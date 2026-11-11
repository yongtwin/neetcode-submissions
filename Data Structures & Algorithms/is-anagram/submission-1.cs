public class Solution {
    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length)
            return false;

        var sArray = s.ToArray();
        var tArray = t.ToArray();

        Array.Sort(sArray);
        Array.Sort(tArray);

        for (int i = 0; i < sArray.Length; i++)
        {
            if (sArray[i].Equals(tArray[i]))
                continue;
            else
                return false;
        }

        return true;
    }
}
