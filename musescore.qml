import QtQuick 2.0
import MuseScore 3.0
import QtWebSockets 1.0

MuseScore {
      menuPath: "Plugins.pluginName"
      description: "Description goes here"
      version: "1.0"
      
   WebSocket {
        id: socket
        url: "ws://localhost:8764/"
        onStatusChanged: if (socket.status == WebSocket.Error) {
                             console.log("Error: " + socket.errorString)
                             Qt.quit()
                         } else if (socket.status == WebSocket.Open) {
                             socket.sendTextMessage("update")
                             Qt.quit()
                         } else if (socket.status == WebSocket.Closed) {
                             Qt.quit()
                         }
        active: true
    }

    
Text 
{
id: messageBox
 text: "Hello world!" 

}
      onRun: { 
            var thisScore = curScore
            console.log(curScore.title)
            console.log(thisScore)
            var res = writeScore( thisScore, "/Users/JonathanStrandberg/Documents/git/websocketTest/new.pdf", "pdf")
            messageBox.text = thisScore.mscoreVersion
            console.log(thisScor)
            console.log(res)
            //Qt.quit()
            }
      }
