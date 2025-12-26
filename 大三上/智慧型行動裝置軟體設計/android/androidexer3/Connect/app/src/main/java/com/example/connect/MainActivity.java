package com.example.connect;

import android.graphics.Bitmap;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkCapabilities;
import android.os.AsyncTask;
import android.os.Bundle;
import android.text.PrecomputedText;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
    private Button btn1,btn2,btn3,btn4,btn5;
    private ImageView iv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ConnectivityManager connectivityManager =(ConnectivityManager) this.getSystemService(MainActivity.CONNECTIVITY_SERVICE);
        Network network = connectivityManager.getActiveNetwork();
        btn1=findViewById(R.id.button);
        btn2=findViewById(R.id.button2);
        btn3=findViewById(R.id.button3);
        btn4=findViewById(R.id.button4);
        btn5=findViewById(R.id.button5);
        iv=findViewById(R.id.imageView);
        btn1.setOnClickListener(btnClick);
        btn2.setOnClickListener(btnClick);
        btn3.setOnClickListener(btnClick);
        btn4.setOnClickListener(btnClick);
        btn5.setOnClickListener(chkNetwork);

        if (network==null)
        {
            Toast.makeText(this,"no network",Toast.LENGTH_SHORT).show();
        }
        else {
            NetworkCapabilities networkCapabilities = connectivityManager.getNetworkCapabilities(network);
            if (networkCapabilities != null && networkCapabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)){
                Toast.makeText(this,"active",Toast.LENGTH_SHORT).show();
            }else{
                Toast.makeText(this,"not working",Toast.LENGTH_SHORT).show();
            }
        }
    }
    private class MyAsyncTask extends AsyncTask<String,Void, Bitmap> {
        @Override
        protected Bitmap doInBackground(String... strings) {
            URL url;
            HttpURLConnection urlConnection=null;
            Bitmap bm=null;
            try {
                url=new URL(params[0]);
                urlConnection=(HttpURLConnection) url.openConnection();
                urlConnection.setRequestMethod("GET");
                urlConnection.connect();
                if(urlConnection.getResponseCode()!=HttpURLConnection.HTTP_OK){
                    urlConnection.disconnect();
                }
            } catch (ProtocolException e) {
                throw new RuntimeException(e);
            } catch (MalformedURLException e) {
                throw new RuntimeException(e);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

    }

    private void downloadImageAndShow(int type,int id) {
    new MyAsyncTask().execute("http://localhost:8080/MyServlet/ImageShower"+type+"&id="+id);
    }
    private View.OnClickListener btnClick=new View.OnClickListener() {
        @Override
        public void onClick(View view) {
        switch (view.getId()) {
            case R.id.button:
                downloadImageAndShow(1,1);
            case R.id.button2:
                downloadImageAndShow(1,2);
            case R.id.button3:
                downloadImageAndShow(2,1);
            case R.id.button4:
                downloadImageAndShow(2,2);
        }

    }
}