import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

ColumnLayout {
    anchors.rightMargin: 5
    anchors.leftMargin: 5
    anchors.bottomMargin: 5
    anchors.topMargin: 5
    spacing: 10
    anchors.fill: parent

    Label {
        id: label
        objectName: "label"
        text: qsTr("Este texto será alterado quando o botão for clicado!")
        Layout.fillWidth: true
        Layout.fillHeight: true
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        wrapMode: Text.WordWrap
        rightPadding: 10
        leftPadding: 10
        padding: 0
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
    }

    TextField {
        id: textfield
        objectName: "textfield"
        text: qsTr("")
        placeholderText: qsTr("Digite algo")
        Layout.fillHeight: false
        Layout.fillWidth: true
        leftPadding: 5
    }

    Button {
        id: button
        objectName: "button"
        text: qsTr("Clique Aqui")
        Layout.fillWidth: true
    }
}

