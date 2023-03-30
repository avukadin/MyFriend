from pkg.Brain import Brain
from pkg.Ears import Ears
from pkg.Mouth import Mouth
from pkg.MyFriend import MyFriend

if __name__ == "__main__":
    brain = Brain()
    friend = MyFriend(brain)
    friend.ears = Ears()
    friend.mouth = Mouth()


    # Testing
    friend.listen()
