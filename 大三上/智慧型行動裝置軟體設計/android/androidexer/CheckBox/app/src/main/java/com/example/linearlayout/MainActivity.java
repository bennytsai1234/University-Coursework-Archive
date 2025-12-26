package com.example.linearlayout;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.RadioGroup;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private CheckBox myCheckBox, myCheckBox2, myCheckBox3;
    private TextView myTextView;
    int amount = 0;
    TextView show_ans;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myCheckBox = findViewById(R.id.checkBox4);
        myCheckBox2 = findViewById(R.id.checkBox3);
        myCheckBox3 = findViewById(R.id.checkBox);
        myTextView = findViewById(R.id.textView8);
        myCheckBox.setOnCheckedChangeListener(myCheckboxListener);
        myCheckBox2.setOnCheckedChangeListener(myCheckboxListener);
        myCheckBox3.setOnCheckedChangeListener(myCheckboxListener);
        RadioGroup radioGroup = findViewById(R.id.deliver);
        radioGroup.setOnCheckedChangeListener(checkRadioGroup);
        show_ans = findViewById(R.id.textView9);

    }

    private final CompoundButton.OnCheckedChangeListener myCheckboxListener = new CompoundButton.OnCheckedChangeListener() {
        @SuppressLint({"NonConstantResourceId", "SetTextI18n"})
        @Override
        public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
            switch (compoundButton.getId()) {
                case R.id.checkBox4:
                    if (myCheckBox.isChecked()) amount += 15;
                    else
                        amount -= 15;
                    myTextView.setText("price:" + amount);
                    break;
                case R.id.checkBox3:
                    if (myCheckBox2.isChecked()) amount += 15;
                    else
                        amount -= 15;
                    myTextView.setText("price:" + amount);
                    break;
                case R.id.checkBox:
                    if (myCheckBox3.isChecked()) amount += 15;
                    else
                        amount -= 15;
                    myTextView.setText("price:" + amount);
                    break;
            }
        }
    };
    private final RadioGroup.OnCheckedChangeListener checkRadioGroup = new RadioGroup.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(RadioGroup radioGroup, int i) {
            if (i == R.id.radioButton) {
                show_ans.setText("選擇內用");
            } else if (i == R.id.radioButton2) {
                show_ans.setText("選擇外送");
            }
        }

    };
}