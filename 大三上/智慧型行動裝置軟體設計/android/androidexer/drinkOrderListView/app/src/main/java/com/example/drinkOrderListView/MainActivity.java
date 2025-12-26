package com.example.drinkOrderListView;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.RadioGroup;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private CheckBox myChkBox;
    private CheckBox myChkBox2;
    private CheckBox myChkBox3;
    private TextView myTxtView, myTxtView2;
    private RadioGroup myRadioGroup;

    private int amount=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myChkBox = findViewById(R.id.checkBox11);
        myChkBox2 = findViewById(R.id.checkBox5);
        myChkBox3 = findViewById(R.id.checkBox6);
        myTxtView = findViewById(R.id.textView6);
        myRadioGroup = findViewById(R.id.deliver);
        myTxtView2 = findViewById(R.id.textView2);

        myChkBox.setOnCheckedChangeListener(myCheckBoxListener);
        myChkBox2.setOnCheckedChangeListener(myCheckBoxListener);
        myChkBox3.setOnCheckedChangeListener(myCheckBoxListener);
        myRadioGroup.setOnCheckedChangeListener(myRadioGruopListener);
    }

    private RadioGroup.OnCheckedChangeListener myRadioGruopListener = new RadioGroup.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(RadioGroup group, int checkedId) {
            if(checkedId == R.id.radioButton2)
                myTxtView2.setText("內用");
            else if(checkedId == R.id.radioButton3)
                myTxtView2.setText("外帶");
        }
    };
    private CompoundButton.OnCheckedChangeListener myCheckBoxListener = new CompoundButton.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
            switch (buttonView.getId()){
                case R.id.checkBox11:
                        if(myChkBox.isChecked()) amount += 40;
                        else amount -=40;
                        myTxtView.setText("總金額:" + amount);
                    break;
                case R.id.checkBox5:
                    if(myChkBox2.isChecked()) amount += 40;
                    else amount -=40;
                    myTxtView.setText("總金額:" + amount);
                    break;
                case R.id.checkBox6:
                    if(myChkBox3.isChecked()) amount += 15;
                    else amount -=15;
                    myTxtView.setText("總金額:" + amount);
                    break;
            }
        }
    };
}