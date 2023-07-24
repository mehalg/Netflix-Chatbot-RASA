# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionSayGenreType(Action):

#     def name(self) -> Text:
#         return "action_say_genre_type"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         genre_type= tracker.get_slot("genre_type")
#         duration_type = tracker.get_slot("duration_type")
        
#         #dispatcher.utter_message(text=["Thanks I'll remember that, and here are some {genre_type} {duration_type} suggestions- Naruto, Jujutsu Kaisen, Chainsawman." if genre_type =='anime' and duration_type =='show';  ])
#         if not genre_type:
#             dispatcher.utter_message(text="Don't know your preferred genre.")
#         elif not duration_type:
#             dispatcher.utter_message(text="Don't know your preferred duration.")
#         elif genre_type=='Anime' and duration_type=='show':
#             dispatcher.utter_message(text=f"Thanks I'll remember that, and here are some {genre_type} {duration_type} suggestions- Naruto, Jujutsu Kaisen, Chainsawman.")
#         elif genre_type=='Anime' and duration_type=='movie':
#             dispatcher.utter_message(text=f"Thanks I'll remember that, and here are some {genre_type} {duration_type} suggestions- Spirited Away, Your Name, Suzume.")
#         elif genre_type=='Thriller/Horror' and duration_type=='movie':
#             dispatcher.utter_message(text=f"Thanks I'll remember that, and here are some {genre_type} {duration_type} suggestions- Shutter Island, Veronica, Escape Room")
#         elif genre_type=='Thriller/Horror' and duration_type=='show':
#             dispatcher.utter_message(text=f"Thanks I'll remember that, and here are some {genre_type} {duration_type} suggestions- The Alienist, The Mindhunter, The Haunting of the Hill House.")
#         else:
#             dispatcher.utter_message(text=f"Your preferred genre is {genre_type}")

#         return []
