package com.example.passwordinputdevice;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private TextView ATMnum;

    private Button btn1, btn2, btn3;
    private Button btn4, btn5, btn6;
    private Button btn7, btn8, btn9;
    private Button btnClr, btn0, btnConfirm;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ATMnum = findViewById(R.id.textView2);
        btn1 = findViewById(R.id.button);
        btn2 = findViewById(R.id.button2);
        btn3 = findViewById(R.id.button3);
        btn4 = findViewById(R.id.button4);
        btn5 = findViewById(R.id.button5);
        btn6 = findViewById(R.id.button6);
        btn7 = findViewById(R.id.button7);
        btn8 = findViewById(R.id.button8);
        btn9 = findViewById(R.id.button9);
        btnClr = findViewById(R.id.button10);
        btn0 = findViewById(R.id.button11);
        btnConfirm = findViewById(R.id.button12);
        btn1.setOnClickListener(myListener);
        btn2.setOnClickListener(myListener);
        btn3.setOnClickListener(myListener);
        btn4.setOnClickListener(myListener);
        btn5.setOnClickListener(myListener);
        btn6.setOnClickListener(myListener);
        btn7.setOnClickListener(myListener);
        btn8.setOnClickListener(myListener);
        btn9.setOnClickListener(myListener);
        btn0.setOnClickListener(myListener);
        btnConfirm.setOnClickListener(myListener);
        btnClr.setOnClickListener(myListener);
    }
    
    private final View.OnClickListener myListener = new View.OnClickListener() {

        @SuppressLint("NonConstantResourceId")
        @Override
        public void onClick(android.view.View v) {
            switch (v.getId()) {
                case R.id.button:
                    displayATM("1");
                    break;
                case R.id.button2:
                    displayATM("2");
                    break;
                case R.id.button3:
                    displayATM("3");
                    break;
                case R.id.button4:
                    displayATM("4");
                    break;
                case R.id.button5:
                    displayATM("5");
                    break;
                case R.id.button6:
                    displayATM("6");
                    break;
                case R.id.button7:
                    displayATM("7");
                    break;
                case R.id.button8:
                    displayATM("8");
                    break;
                case R.id.button9:
                    displayATM("9");
                    break;
                case R.id.button11:
                    displayATM("0");
                    break;
                case R.id.button10:
                    new AlertDialog.Builder(MainActivity.this)
                            .setTitle("clear?")
                            .setIcon(R.mipmap.ic_launcher_round)
                            .setMessage("confirm to clear?")
                            .setNegativeButton("cancel", (dialogInterface, i) -> {

                            })
                            .setPositiveButton("YES", (dialogInterface, i) -> ATMnum.setText(""))
                            .show();
                    break;
                case R.id.button12:
                    String password = "123456";
                    String str = ATMnum.getText().toString();
                    Toast toast1;
                    if(str.equals(password)){
                        toast1 = Toast.makeText(MainActivity.this, "密碼正確", Toast.LENGTH_LONG);
                    }
                    else{
                        toast1 = Toast.makeText(MainActivity.this, "密碼錯誤", Toast.LENGTH_LONG);
                    }
                    toast1.show();

            }
        }
        @SuppressLint("SetTextI18n")
        private void displayATM(String s) {
            String str = ATMnum.getText().toString();
            ATMnum.setText(str + s);
        }
    };
}

