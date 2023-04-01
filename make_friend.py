from pkg.Brain import Brain
from pkg.Ears import Ears
from pkg.Mouth import Mouth
from pkg.MyFriend import MyFriend

from config import GPT_MODEL

if __name__ == "__main__":
    brain = Brain('Francis', GPT_MODEL)
    friend = MyFriend(brain)
    friend.ears = Ears()
    friend.mouth = Mouth()

    friend.start()
