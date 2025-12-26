package com.example.test6;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private TextView txtKm;
    private EditText txtInput;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtKm = findViewById(R.id.textView2);
        Button myButton = findViewById(R.id.button);
        txtInput = findViewById(R.id.editTextNumber);
        myButton.setOnClickListener(myOnClickListener);
    }
    private final Button.OnClickListener myOnClickListener=
            new Button.OnClickListener() {
                @SuppressLint("SetTextI18n")
                @Override
                public void onClick(View view) {
                    double miles = Double.parseDouble(txtInput.getText().toString());
                    double km = miles * 1.61;
                    txtKm.setText("時速= " + km + " 公里");
                }
            };
}
