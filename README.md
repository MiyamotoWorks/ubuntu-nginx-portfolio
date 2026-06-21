# Ubuntu 26.04 LTS WebServer (Nginx) 構築プロジェクト

仮想環境（VirtualBox）上にLinuxサーバーを構築し、Webサーバー（Nginx）の導入とホストOSからのアクセス検証を行いました。

## 構成環境
- **ホストOS**: Windows
- **ゲストOS**: Ubuntu Server 26.04 LTS (VirtualBox)
- **Webサーバー**: Nginx

## 実施内容
1. SSHによるリモート接続環境の開通（IP: 192.168.11.10）
2. Nginxのインストールおよびサービス起動確認
3. ホストOSブラウザからの疎通確認テスト

## 検証エビデンス（稼働証明）

### 1. Nginx サービス稼働確認
サーバー上でNginxが正常に常駐・起動している状態です。
![Nginx Status](nginx-status-running.png)

### 2. ホストOSからのブラウザ疎通確認
Windows側のブラウザからUbuntuサーバーへ接続し、Webページが表示されることを確認しました。
![Browser Access](browser-access-success.png)
