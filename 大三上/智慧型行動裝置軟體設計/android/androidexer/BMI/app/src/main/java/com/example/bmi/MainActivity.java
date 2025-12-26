package com.example.bmi;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private TextView txt;
    private EditText txtInput1;
    private EditText txtInput2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txt = findViewById(R.id.textView5);
        Button myButton = findViewById(R.id.button);
        txtInput1 = findViewById(R.id.editTextNumber2);
        txtInput2 = findViewById(R.id.editTextNumber3);
        myButton.setOnClickListener(myOnClickListener);
    }
    private final Button.OnClickListener myOnClickListener=
            new Button.OnClickListener() {
                @SuppressLint("SetTextI18n")
                @Override
                public void onClick(View view) {
                    double cm1 = Double.parseDouble(txtInput1.getText().toString());
                    double kg1 = Double.parseDouble(txtInput2.getText().toString());
                    double bmi= (kg1*10000)/(cm1*cm1);
                    txt.setText(" " + bmi + " ");
                }
            };

}