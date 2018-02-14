import os

import pygame


BASE_PATH = 'resources/sounds/'


class SoundController:
    GAME_INTRO = 'game_intro.wav'
    START_GAME = 'start_game.wav'
    RACQUET = 'return_racquet.wav'
    GAME_OVER = 'game_over.wav'
    THUD = 'thud.wav'

    @staticmethod
    def _stop_all_sound():
        pygame.mixer.stop()

    @staticmethod
    def _load_sound_file(fname):
        return pygame.mixer.Sound(fname)

    @classmethod
    def play_intro(cls):
        cls._stop_all_sound()
        fname = os.path.join(BASE_PATH, cls.GAME_INTRO)
        sound = cls._load_sound_file(fname)
        sound.play()

    @classmethod
    def play_racquet(cls):
        cls._stop_all_sound()
        fname = os.path.join(BASE_PATH, cls.RACQUET)
        sound = cls._load_sound_file(fname)
        sound.play()

    @classmethod
    def play_game_over(cls):
        cls._stop_all_sound()
        fname = os.path.join(BASE_PATH, cls.GAME_OVER)
        sound = cls._load_sound_file(fname)
        sound.play()

    @classmethod
    def play_new_game(cls):
        cls._stop_all_sound()
        fname = os.path.join(BASE_PATH, cls.START_GAME)
        sound = cls._load_sound_file(fname)
        sound.play()

    @classmethod
    def play_thud(cls):
        cls._stop_all_sound()
        fname = os.path.join(BASE_PATH, cls.THUD)
        sound = cls._load_sound_file(fname)
        sound.play()
