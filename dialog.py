answers = {
    'Hello': {'text':'Hello'},
    '/start': {'text':'I am the best boat in the world!'},
    '/menu': {'text':'Main menu', 
              'attachments':[
                  {
                      "type": "inline_keyboard", 
                      "payload": {
                          "buttons": [
                              [
                                  {
                                      "type": "callback",
                                      "text": "Test1!",
                                      "payload": "button1 pressed"
                                  }
                              ], 
                              [
                                  {
                                      "type": "callback",
                                      "text": "Test2!",
                                      "payload": "button2 pressed"
                                  }
                              ]
                          ]
                      }
                  }
              ]
    }
}