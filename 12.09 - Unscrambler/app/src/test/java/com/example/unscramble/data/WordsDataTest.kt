package com.example.unscramble.data

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class WordsDataTest {

    @Test
    fun constants_areCorrect() {
        assertEquals(10, MAX_NO_OF_WORDS)
        assertEquals(20, SCORE_INCREASE)
    }

    @Test
    fun allWords_isNotEmpty() {
        assertTrue(allWords.isNotEmpty())
    }

    @Test
    fun allWords_hasAtLeastMaxNoOfWords() {
        assertTrue(allWords.size >= MAX_NO_OF_WORDS)
    }

    @Test
    fun allWords_allAreLowerCase() {
        allWords.forEach { word ->
            assertEquals(
                "Слово '$word' должно быть в нижнем регистре",
                word.lowercase(),
                word
            )
        }
    }

    @Test
    fun allWords_allAreNotBlank() {
        allWords.forEach { word ->
            assertTrue("Пустое слово в allWords", word.isNotBlank())
        }
    }

    @Test
    fun allWords_noDuplicates() {
        val asList = allWords.toList()
        assertEquals(asList.size, asList.toSet().size)
    }
}