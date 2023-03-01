import java.util.HashMap;

class UserSolution {
    final int MAX_MAKE_LIST = 10;
    final int MAX_LENGTH = 200000;
    final int MAX_ADDRESS = 6000;
    final int MAX_CHANGE = 110000;
    int arNumber; // 배열이 실제로 저장되는 인덱스
    int[][] realAr; // 실제 배열 저장

    int addressNumber; // 배열의 인덱스
    HashMap<String, Integer> address; // 배열의 이름과 인덱스 저장

    Log[] log; // 진짜 로그의 내용
    int changeNumber; // 로그의 번호
    int[] lastChange; // 배열의 마지막 로그 번호
    int[] prevChange; // 로그의 이전 로그 번호

    void init() {
        arNumber = 0;
        realAr = new int[MAX_MAKE_LIST + 1][MAX_LENGTH + 1];

        addressNumber = 0;
        address = new HashMap<>();

        changeNumber = 0;
        log = new Log[MAX_CHANGE + 1];
        lastChange = new int[MAX_ADDRESS + 1];
        prevChange = new int[MAX_CHANGE + 1];
    }

    String getName(char[] name) {
        String x = "";
        for (int i=0;name[i]!=0;i++){
            x += name[i];
        }
        return x;
    }

    void makeList(char[] _mName, int mLength, int[] mListValue) {
        String mName = getName(_mName);
        System.arraycopy(mListValue, 0, realAr[arNumber], 0, mLength);
        arNumber++;

        address.put(mName, addressNumber);
        addressNumber++;

        log[changeNumber] = new Log(-1, arNumber - 1);

        prevChange[changeNumber] = -1; // 배열이 생성됨을 의미
        lastChange[address.get(mName)] = changeNumber;
        changeNumber++;
    }

    void copyList(char[] _mDest, char[] _mSrc, boolean mCopy) {
        String mDest = getName(_mDest);
        String mSrc = getName(_mSrc);
        if (mCopy) {
            address.put(mDest, addressNumber);
            addressNumber++;

            log[changeNumber] = new Log(-1, -1); // 배열이 깊은 복사됨을 의미

            prevChange[changeNumber] = lastChange[address.get(mSrc)];
            lastChange[address.get(mDest)] = changeNumber;
            changeNumber++;
        } else {
            address.put(mDest, address.get(mSrc)); // 같은 주소 저장
        }
    }

    void updateElement(char[] _mName, int mIndex, int mValue) {
        String mName = getName(_mName);

        log[changeNumber] = new Log(mIndex, mValue); // mIndex의 값을 mValue로 바꿨음을 의미

        prevChange[changeNumber] = lastChange[address.get(mName)];
        lastChange[address.get(mName)] = changeNumber;
        changeNumber++;
    }

    int element(char[] _mName, int mIndex) {
        String mName = getName(_mName);
        int logIndex = lastChange[address.get(mName)];

        while (true) {
            if (prevChange[logIndex] == -1) {
                return realAr[log[logIndex].second][mIndex];
            }
            if (log[logIndex].first == mIndex) {
                return log[logIndex].second;
            }
            logIndex = prevChange[logIndex];
        }
    }

    class Log {
        int first;
        int second;

        public Log(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
}
