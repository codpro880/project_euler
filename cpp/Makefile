.PHONY: all clean
CPP_FILES := $(shell find . -name "*.cpp")
TARGETS := $(CPP_FILES:.cpp=.out)

#CARD_CPP_FILES = $(shell find . -name "*.cpp" ! -name "*_test.cpp")
# $(info $$CARD_CPP_FILES is [${CARD_CPP_FILES}]) # DEBUG
#OBJ_TARGETS = $(CARD_CPP_FILES:.cpp=.o)
# $(info $$CARD_CPP_FILES is [${CARD_CPP_FILES}]) # DEBUG

%.out: %.cpp
	$(CXX) -std=c++17 $< -o $@

all: $(TARGETS)

clean:
	rm -f *.out