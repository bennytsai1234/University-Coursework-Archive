package com.example.midterm;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class Second extends AppCompatActivity {
    private int[] myImgList={R.drawable.t152,R.drawable.t157,R.drawable.t161};
    String[] titles = {"恆吉宮媽祖廟", "南興打鐵街", "靈巖山寺"};
    String[] descriptions = {"Description 1", "Description 2", "Description 3"};
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout);
        ListView myListView=findViewById(R.id.Listview);
        Second.CustomListAdapter secAdapter =new CustomListAdapter(this, titles, descriptions, myImgList);
        myListView.setAdapter(secAdapter);
        myListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Intent intent = new Intent();
                intent.setClass(Second.this, third.class);
                startActivity(intent);
            }
        });

    }
    public class CustomListAdapter extends BaseAdapter {
        private Context context;
        private String[] itemTitles;
        private String[] itemDescriptions;
        private int[] itemImages;

        public CustomListAdapter(Context context, String[] itemTitles, String[] itemDescriptions, int[] itemImages) {
            this.context = context;
            this.itemTitles = itemTitles;
            this.itemDescriptions = itemDescriptions;
            this.itemImages = itemImages;
        }

        @Override
        public int getCount() {
            return itemTitles.length;
        }

        @Override
        public Object getItem(int position) {
            return itemTitles[position];
        }

        @Override
        public long getItemId(int position) {
            return position;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            View itemView = inflater.inflate(R.layout.custom_list_item, parent, false);

            ImageView imageView = itemView.findViewById(R.id.imageView);
            TextView titleTextView = itemView.findViewById(R.id.titleTextView);
            TextView descriptionTextView = itemView.findViewById(R.id.descriptionTextView);

            imageView.setImageResource(itemImages[position]);
            titleTextView.setText(itemTitles[position]);
            descriptionTextView.setText(itemDescriptions[position]);

            return itemView;
        }
    }
}