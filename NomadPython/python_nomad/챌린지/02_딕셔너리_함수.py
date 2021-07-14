# dictionary에 내용 추가
def add_to_dict(dictionary, key=None, value=None):
  # dictonary 타입일 경우에만 체크
  if type(dictionary) is dict:
    if value == None:
      print('You need to send a word and a Definition.')
    else:
      # 값이 있는 dictionary에 key값이 존재하는지 체크
      if key in dictionary:
        print(key, 'is already on the dictionary. Won\'t add.')
      else:
        # dictionary에 key value값을 입력
        dictionary[key] = value
        print(key, 'has been added.')
  # type이 dictionary가 아닐 경우에는 진행하지 않음
  else:
    non_exist(dictionary)
    # print('You need to send a dictionary. You sent:', type(dict))


# dictionary에 key가 존재하면, value값 가져오기
def get_from_dict(dictionary, key=None):
  # dictionary 타입일 경우에만 체크
  if type(dictionary) is dict:
    # key값을 파라미터로 전달받은 경우에만 검색 진행
    if key == None:
      print('You need to send a word to search for.')
    else:
      # key값이 존재하면 해당하는 value값을 알려줌
      if key in dictionary:
        print(key, ':', dictionary.get(key))
      else:
        print(key, 'was not found in this dict')
  else:
    non_exist(dictionary)


# dictionary 내용 수정
def update_word(dictionary, key=None, value=None):
  # dictionary 타입일 경우에만 체크
  if type(dictionary) is dict:
    # key, value값을 모두 전달받은 경우에만 업데이트 진행
    if value == None:
      print('You need to send a word and a definition to update.')
    else:
      # dictionary에 해당 key가 존재하는 경우에만 value값을 update 
      if key in dictionary:
        dictionary[key] = value
        print(key, 'has been updated to:', value)
      else:
        print(key, 'is not on the dict. Can\'t update non-existing word.')
  else:
    non_exist(dictionary)


# dictionary 내용 삭제
def delete_from_dict(dictionary, key=None):
  # dictionary 타입일 경우에만 체크
  if type(dictionary) is dict:
    # key값을 파라미터로 전달받은 경우에만 삭제 체크 진행
    if key == None:
      print('You need to specify a word to delete.')
    else:
      if key in dictionary:
        # key값이 존재하는 경우에 dictionary 에서 삭제(del 함수)
        del dictionary[key]
        print(key, 'has been deleted.')
      else:
        print(key, 'is not in this dict. Won\'t delete.')
  else:
    non_exist(dictionary)


# 공통된 타입체크 분리
def non_exist(dictionary):
    print('You need to send a dictionary. You sent:', type(dictionary))

my_english_dict = {}


###########################################################################
print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")

print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")