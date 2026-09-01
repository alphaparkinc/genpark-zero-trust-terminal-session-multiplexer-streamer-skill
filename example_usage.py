from client import ZeroTrustTerminalSessionMultiplexerStreamerClient

def main():
    client = ZeroTrustTerminalSessionMultiplexerStreamerClient()
    res = client.initiate_secure_terminal_session('dev-box-arm64')
    print('Terminal Multiplexer Streamer: ' + res['session_stream_id'] + ' on ' + res['host'])
    print('WebRTC E2E Encrypted: ' + str(res['p2p_webrtc_e2e_encrypted']) + ' | Cast Active: ' + str(res['asciinema_cast_recording_active']))
    print('Share URL: ' + res['secure_share_webrtc_endpoint_url'])
    print('Replay URL: ' + res['session_cast_replay_url'])

if __name__ == '__main__':
    main()
