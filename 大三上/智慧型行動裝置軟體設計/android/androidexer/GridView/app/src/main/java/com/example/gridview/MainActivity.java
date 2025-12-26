package com.example.gridview;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.BaseAdapter;
import android.widget.GridView;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private final int[] myImgList={ R.drawable.bubbletea,R.drawable.donguatea,R.drawable.greentea,R.drawable.guayuantea,R.drawable.pooltea,R.drawable.reatea};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView myImgShow = findViewById(R.id.imageView3);
        GridView myGridView = findViewById(R.id.gridView);
        MyAdapter adapter=new MyAdapter(this);
        myGridView.setAdapter(adapter);
        myGridView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                myImgShow.setImageResource(myImgList[position]);
            }
        }
        );
    }
    class MyAdapter extends BaseAdapter{
        private final Context mContext;
        public MyAdapter(Context c){
            mContext=c;
        }
        @Override
        public int getCount(){
            return myImgList.length;
        }
        @Override
        public Object getItem(int position){
            return position;
        }
        @Override
        public long getItemId(int position){
            return position;
        }
        @Override
        public View getView(int position, View convertView, ViewGroup parent){
            ImageView iv=new ImageView(mContext);
            iv.setImageResource(myImgList[position]);
            iv.setScaleType(ImageView.ScaleType.FIT_CENTER);
            iv.setLayoutParams(new ViewGroup.LayoutParams(320,240));
            return  iv;
        }
    }

}