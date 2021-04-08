import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String greetings = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              RaisedButton(
                onPressed: _launchDashboardURL,
                child: Text(
                  'Dashboard',
                  style: TextStyle(color: Colors.white),
                ),
                color: Colors.pinkAccent,
              ),
              RaisedButton(
                onPressed: _launchHeartURL,
                child: Text(
                  'Heart Rate',
                  style: TextStyle(color: Colors.white),
                ),
                color: Colors.greenAccent,
              ),
              RaisedButton(
                onPressed: _launchOxygenURL,
                child: Text(
                  'Oxygen Saturaion',
                  style: TextStyle(color: Colors.white),
                ),
                color: Colors.teal,
              ),
            ],
          ),
        ),
      ),
    );
  }

  _launchDashboardURL() async {
//     const url = 'http://192.168.0.120:5000/heartRate';
//    const url = 'http://10.10.10.85:5000/heartRate';
    const url = "http://genhicu.infinityfreeapp.com";
    if (await canLaunch(url)) {
      await launch(
        url,
        forceWebView: true,
        forceSafariVC: true,
        enableJavaScript: true,
      );
    } else {
      throw 'Could not launch $url';
    }
  }

  _launchHeartURL() async {
//     const url = 'http://192.168.0.120:5000/heartRate';
    const url = 'http://10.10.10.85:5000/heartRate';
    // const url = "http://www.google.com";
    if (await canLaunch(url)) {
      await launch(url,
          forceWebView: true, forceSafariVC: true, enableJavaScript: true);
    } else {
      // throw 'Could not launch $url';
       Text(' Server not respond');
    }
  }

  _launchOxygenURL() async {
    const url = 'http://192.168.0.120:5000/oxygenSaturation';
//    const url = 'http://10.10.10.85:5000/oxygenSaturation';
    if (await canLaunch(url)) {
      await launch(url, forceWebView: true, enableJavaScript: true);
    } else {
      throw 'Could not launch $url';
    }
  }
}
