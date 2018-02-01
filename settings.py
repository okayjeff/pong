# Display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_RESOLUTION = (WINDOW_WIDTH, WINDOW_HEIGHT)
HALF_WINDOW_WIDTH = WINDOW_WIDTH // 2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT // 2

FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Arena Config
LINE_THICKNESS = 4
CENTER_LINE_THICKNESS = LINE_THICKNESS // 2
ARENA_BORDER_THICKNESS = LINE_THICKNESS * 2
ARENA_LINE_COLOR = WHITE
ARENA_BGCOLOR = BLACK

LEFT_EDGE = LINE_THICKNESS
RIGHT_EDGE = WINDOW_WIDTH - LINE_THICKNESS
TOP_EDGE = LINE_THICKNESS
BOTTOM_EDGE = WINDOW_HEIGHT - LINE_THICKNESS
TOP_LEFT = (0, 0)
BOTTOM_RIGHT = (WINDOW_WIDTH, WINDOW_HEIGHT)
DEAD_CENTER = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
MID_TOP = (WINDOW_WIDTH//2, TOP_EDGE)
MID_BOTTOM = (WINDOW_WIDTH//2, BOTTOM_EDGE)

# Ball Config
BALL_COLOR = WHITE
BALL_THICKNESS = LINE_THICKNESS * 2

# Paddle Config
PADDLE_COLOR = WHITE
PADDLE_SIZE = 50
PADDLE_THICKNESS = LINE_THICKNESS * 2
PADDLE_OFFSET = 20

# Game Config
WINNING_SCORE = 5
DEFAULT_SPEED = -3

PLAYER_ONE = 1
PLAYER_TWO = 2

# Font
DEFAULT_FONT_SIZE = 14
DEFAULT_FONT = 'Courier'
ANTIALIAS = True
TITLE_FONT_SIZE = DEFAULT_FONT_SIZE * 5
SUBTITLE_FONT_SIZE = DEFAULT_FONT_SIZE

# Clock
CLOCK_WIDTH = 75
CLOCK_HEIGHT = 25
CLOCK_FONT_SIZE = DEFAULT_FONT_SIZE + 6
TIME_FORMAT = '%M:%S'

# Announcement
ANNOUNCEMENT_WIDTH = 200
ANNOUNCEMENT_HEIGHT = 75
ANNOUNCEMENT_BGCOLOR = WHITE
ANNOUNCEMENT_FONT_COLOR = BLACK
ANNOUNCEMENT_FONT_SIZE = DEFAULT_FONT_SIZE + 2

# Game Modes (ball speeds)
EASY = DEFAULT_SPEED
MEDIUM = DEFAULT_SPEED - 2
HARD = DEFAULT_SPEED - 4

GAME_NAME = 'PyPong'
RECORDS_FILENAME = 'records.txt'