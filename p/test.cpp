#include <iostream>
#include <string>

using namespace std;

template <class T> constexpr std::string_view
type_name()
{
    using namespace std;
#ifdef __clang__
    string_view p = __PRETTY_FUNCTION__;
    return string_view(p.data() + 34, p.size() - 34 - 1);
#elif defined(__GNUC__)
    string_view p = __PRETTY_FUNCTION__;
#  if __cplusplus < 201402
    return string_view(p.data() + 36, p.size() - 36 - 1);
#  else
    return string_view(p.data() + 49, p.find(';', 49) - 49);
#  endif
#elif defined(_MSC_VER)
    string_view p = __FUNCSIG__;
    return string_view(p.data() + 84, p.size() - 84 - 7);
#endif
}

int main() {
    string str;
    cout << type_name<decltype(str)>() << endl;

    string str1 = "";
    cout << (str1 == "") << endl;

    string str2[] = { "a", "b", "c", "d", "e" };
    cout << type_name<decltype(str2[0])>() << endl;
    cout << type_name<decltype(str2)>() << endl;
    cout << type_name<decltype(str2 + 0)>() << endl;
    cout << type_name<decltype(&str[2])>() << endl;
}