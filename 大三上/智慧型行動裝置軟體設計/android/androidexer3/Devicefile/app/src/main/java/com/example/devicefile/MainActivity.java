package com.example.devicefile;

import android.app.AlertDialog;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private Button clr;
    private TextView edtname;
    private SharedPreferences spf;
    private String name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button end = findViewById(R.id.button);
        clr = findViewById(R.id.button2);
        TextView txtname = findViewById(R.id.textView);
        edtname = findViewById(R.id.editTextText);

        end.setOnClickListener(lis);
        clr.setOnClickListener(lis);

        spf = getSharedPreferences("preFile",MODE_PRIVATE);
        name = spf.getString("name","");

        String msg;
        if(name.equals(""))
        {
            txtname.setVisibility(TextView.VISIBLE);
            edtname.setVisibility(TextView.VISIBLE);
            clr.setVisibility(Button.INVISIBLE);
            msg = "welcome";
        }
        else
        {
            txtname.setVisibility(TextView.INVISIBLE);
            edtname.setVisibility(TextView.INVISIBLE);
            clr.setVisibility(Button.VISIBLE);
            msg = "welcome，" + name;
        }

        new AlertDialog.Builder(MainActivity.this)
                .setTitle("welcome")
                .setMessage(msg)
                .setPositiveButton("confine", (dialogInterface, i) -> {

                }).show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        if(name.equals(""))
        {
            FileOutputStream FOS;
            try {
                FOS = openFileOutput("text.txt",MODE_PRIVATE);
            } catch (FileNotFoundException e) {
                throw new RuntimeException(e);
            }
            BufferedOutputStream buffer = new BufferedOutputStream(FOS);
            try {
                buffer.write(edtname.getText().toString().getBytes());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            try {
                buffer.close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    private final View.OnClickListener lis = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            int id = view.getId();
            if(id == R.id.button){
                finish();
            }
            if(id == R.id.button2)
            {
                if(!name.equals(""))
                {
                    spf.edit()
                            .clear()
                            .apply();
                    Toast.makeText(getApplicationContext(), "clear", Toast.LENGTH_LONG).show();
                }
                clr.setVisibility(Button.INVISIBLE);
            }
        }
    };
}