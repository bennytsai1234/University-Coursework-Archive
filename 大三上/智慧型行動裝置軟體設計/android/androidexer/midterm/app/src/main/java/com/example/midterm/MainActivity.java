package com.example.midterm;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.BaseAdapter;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private int[] myImgList={R.drawable.landmarks_0002,R.drawable.mfood_03,R.drawable.mhotel_02,R.drawable.gitf_0003};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(getApplicationContext(),"onCreate(1)",Toast.LENGTH_LONG).show();
        GridView myGridView=findViewById(R.id.gridview);
        MyAdapter adapter=new MyAdapter(this);
        myGridView.setAdapter(adapter);
        myGridView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Intent intent = new Intent();
                intent.setClass(MainActivity.this, Second.class);
                startActivity(intent);
            }
        });
    }
    class MyAdapter extends BaseAdapter{
        private Context mContext;
        public MyAdapter(Context c){
            mContext=c;
        }
        @Override
        public int getCount() {
            return  myImgList.length;
        }

        @Override
        public Object getItem(int i) {
            return i;
        }

        @Override
        public long getItemId(int i) {
            return i;
        }

        @Override
        public View getView(int i, View view, ViewGroup viewGroup) {
            ImageView iv=new ImageView(mContext);
            iv.setImageResource(myImgList[i]);
            iv.setScaleType(ImageView.ScaleType.FIT_CENTER);
            iv.setLayoutParams(new ViewGroup.LayoutParams(480,360));
            return iv;
        }
    };
    @Override
    protected void onStart() {
        super.onStart();

        Toast.makeText(getApplicationContext(),"onStart(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onResume() {
        super.onResume();

        Toast.makeText(getApplicationContext(),"onResume(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast.makeText(getApplicationContext(),"onRestart(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onPause() {
        super.onPause();

        Toast.makeText(getApplicationContext(),"onPause(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onStop() {
        super.onStop();

        Toast.makeText(getApplicationContext(),"onStop(1)",Toast.LENGTH_LONG).show();

    }

    @Override
    protected void onDestroy() {
        Toast.makeText(getApplicationContext(),"onDestroy(1)",Toast.LENGTH_LONG).show();

        super.onDestroy();

    }
}