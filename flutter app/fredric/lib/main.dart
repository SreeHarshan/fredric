import 'package:flutter/material.dart';
import 'package:device_preview/device_preview.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return App();
  }
}
/*
void main() {
  runApp(App());
}
*/

void main() => runApp(
      DevicePreview(
        enabled: true,
        builder: (context) => MyApp(), // Wrap your app
      ),
    );

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Fredric',
        theme: ThemeData(
          colorScheme: ColorScheme.dark(),
        ),
        home: Scaffold(
            body: Center(
                child: Container(
                    margin: const EdgeInsets.all(15.0),
                    decoration:
                        BoxDecoration(border: Border.all(color: Colors.green)),
                    // ignore: prefer_const_literals_to_create_immutables
                    child: Column(
                      children: <Widget>[
                        const Text(
                          "Fredric",
                          style: TextStyle(
                            color: Color(0xffcacaca),
                            fontSize: 23,
                          ),
                        ),
                        core()
                      ],

                      mainAxisAlignment: MainAxisAlignment
                          .center, //Center Column contents vertically,
                      crossAxisAlignment: CrossAxisAlignment
                          .center, //Center Column contents horizontally,
                    )))));
  }
}

class core extends StatefulWidget {
  const core({Key? key}) : super(key: key);

  @override
  _corestate createState() => _corestate();
}

class _corestate extends State<core> {
  List<String> periods = [];

  _corestate() {
    for (int i = 0; i <= 5; i++) {
      periods[i] = "None";
    }
  }
  void update_class() {
    //TODO do this
    periods[0] = "eng";
  }

  @override
  Widget build(BuildContext context) {
    return Column(children: <Widget>[
      const Text(
        "1",
        style: TextStyle(
          color: Color(0xffcacaca),
          fontSize: 15,
        ),
      ),
      Text(
        periods[0],
        // ignore: prefer_const_constructors
        style: TextStyle(
          color: const Color(0xffcacaca),
          fontSize: 15,
        ),
      )
    ]);
  }
}
