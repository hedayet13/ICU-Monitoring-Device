import 'package:flutter/material.dart';
import 'package:icuchart/homePage.dart';
import 'package:shimmer/shimmer.dart';

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();

    _mockChcek().then((status) {
      if (status) {
        _navigateToHome();
      }
    });
  }

  Future<bool> _mockChcek() async {
    await Future.delayed(Duration(milliseconds: 4000), () {});

    return true;
  }

  void _navigateToHome() {
    Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (BuildContext context) => MyHomePage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
      child: Stack(
        alignment: Alignment.center,
        children: [
          Shimmer.fromColors(
              child: Container(
                child: Center(
                  child: Text(
                    "ICU Monitoring..",
                    style: TextStyle(
                        fontSize: 40,
                        fontFamily: 'Inkfree',
                        fontWeight: FontWeight.bold,
                        shadows: [
                          Shadow(
                              blurRadius: 18.0,
                              color: Colors.black87,
                              offset: Offset.fromDirection(120, 12))
                        ]),
                  ),
                ),
              ),
              baseColor: Colors.teal,
              highlightColor: Colors.green)
        ],
      ),
    ));
  }
}
