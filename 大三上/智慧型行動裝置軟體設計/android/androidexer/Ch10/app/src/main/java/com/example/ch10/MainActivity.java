package com.example.ch10;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private final String TAG="myLOG";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d(TAG,"onCreate");
        Toast.makeText(getApplicationContext(),"onCreate(1)",Toast.LENGTH_LONG).show();
        Button btnDial = findViewById(R.id.button);
        Button btnFinish = findViewById(R.id.button3);
        Button btnPage2 = findViewById(R.id.button2);
        btnDial.setOnClickListener(myClickListener);
        btnPage2.setOnClickListener(myClickListener);
    }
    private final View.OnClickListener myClickListener= view -> {
        if (view.getId()==R.id.button){
            Uri uri=Uri.parse("tel:0911123456");
            Intent intent=new Intent(Intent.ACTION_DIAL,uri);
            startActivity(intent);
        }
        else if (view.getId()==R.id.button2){
            Intent intent=new Intent();
            intent.setClass(MainActivity.this, Second.class);
            startActivity(intent);
        }
        else if (view.getId()==R.id.button3) {
            finish();
        }
    };
    @Override
    protected void onStart() {
        super.onStart();
        Log.d(TAG,"onStart");
        Toast.makeText(getApplicationContext(),"onStart(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d(TAG,"onResume");
        Toast.makeText(getApplicationContext(),"onResume(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d(TAG,"onRestart");
        Toast.makeText(getApplicationContext(),"onRestart(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d(TAG,"onPause");
        Toast.makeText(getApplicationContext(),"onPause(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d(TAG,"onStop");
        Toast.makeText(getApplicationContext(),"onStop(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onDestroy() {
        Toast.makeText(getApplicationContext(),"onDestroy(1)",Toast.LENGTH_LONG).show();
        Log.d(TAG,"onDestroy");
        super.onDestroy();

    }
}