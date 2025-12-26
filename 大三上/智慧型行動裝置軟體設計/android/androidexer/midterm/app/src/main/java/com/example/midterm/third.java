package com.example.midterm;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.BaseAdapter;
import android.widget.GridView;
import android.widget.ImageView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class third extends AppCompatActivity {
    private final int[] img ={R.drawable.map_003,R.drawable.phoneee};
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.weblayout);

        WebView webView = findViewById(R.id.webview);
        webView.loadUrl("https://fundanantou.pixnet.net/blog/post/214535954-%E3%80%90%E6%9B%B8%E5%8C%85%E5%AE%A2super-go%E3%80%91%2A%E9%81%8A%E5%9F%94%E9%87%8C%22%E6%A1%83%E7%B1%B3%E7%94%9F%E6%85%8B%E6%9D%91-%E3%80%88%E8%B7%AF%E7%B7%9A");
        GridView myGridView=findViewById(R.id.webgrid);
        third.My3Adapter adapter3=new third.My3Adapter(this);
        myGridView.setAdapter(adapter3);
        myGridView.setOnItemClickListener((adapterView, view, i, l) -> {
            Uri uri = Uri.parse("tel:0911123456");
            Intent intent = new Intent(Intent.ACTION_DIAL, uri);
            startActivity(intent);
        });

    }
    class My3Adapter extends BaseAdapter {
        private final Context mContext;
        public My3Adapter(Context c){
            mContext=c;
        }
        @Override
        public int getCount() {
            return  img.length;
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
            iv.setImageResource(img[i]);
            iv.setScaleType(ImageView.ScaleType.FIT_CENTER);
            iv.setLayoutParams(new ViewGroup.LayoutParams(240,180));
            return iv;
        }
    }

}
