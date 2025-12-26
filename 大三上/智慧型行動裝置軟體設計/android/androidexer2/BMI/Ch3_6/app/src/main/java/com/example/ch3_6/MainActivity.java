package com.example.ch3_6;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView myTextView;
    private EditText myEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        myTextView = findViewById(R.id.textView2);
        Button myButton = findViewById(R.id.button);
        myEditText = findViewById(R.id.editTextNumber);

        myButton.setOnClickListener(myOnClickListener);
    }

    private final View.OnClickListener myOnClickListener = new View.OnClickListener() {
        @SuppressLint("SetTextI18n")
        @Override
        public void onClick(View v) {
            double miles = Double.parseDouble(myEditText.getText().toString());
            double km = miles*1.61;
            myTextView.setText("時速" + km + "公里");
        }
    };
}