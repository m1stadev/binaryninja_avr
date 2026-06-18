from .chip import Chip


class IOCAN64(Chip):
    """
    AT90CAN64
    """

    CHIP_ALIASES = ["iocan64", "AT90CAN64"]
    RAM_SIZE = 4096
    ROM_SIZE = 64 * 1024
    INTERRUPT_VECTOR_SIZE = 4

    # https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/doc7679.pdf
    # Chapter 29
    IO_REGISTERS = {
        0x00: 'PINA',
        0x01: 'DDRA',
        0x02: 'PORTA',
        0x03: 'PINB',
        0x04: 'DDRB',
        0x05: 'PORTB',
        0x06: 'PINC',
        0x07: 'DDRC',
        0x08: 'PORTC',
        0x09: 'PIND',
        0x0A: 'DDRD',
        0x0B: 'PORTD',
        0x0C: 'PINE',
        0x0D: 'DDRE',
        0x0E: 'PORTE',
        0x0F: 'PINF',
        0x10: 'DDRF',
        0x11: 'PORTF',
        0x12: 'PING',
        0x13: 'DDRG',
        0x14: 'PORTG',
        0x15: 'TIFR0',
        0x16: 'TIFR1',
        0x17: 'TIFR2',
        0x18: 'TIFR3',
        0x1C: 'EIFR',
        0x1D: 'EIMSK',
        0x1E: 'GPIOR0',
        0x1F: 'EECR',
        0x20: 'EEDR',
        0x21: 'EEARL',
        0x22: 'EEARH',
        0x23: 'GTCCR',
        0x24: 'TCCR0A',
        0x26: 'TCNT0',
        0x27: 'OCR0A',
        0x2A: 'GPIOR1',
        0x2B: 'GPIOR2',
        0x2C: 'SPCR',
        0x2D: 'SPSR',
        0x2E: 'SPDR',
        0x30: 'ACSR',
        0x31: 'OCDR',
        0x33: 'SMCR',
        0x34: 'MCUSR',
        0x35: 'MCUCR',
        0x37: 'SPMCSR',
        0x3B: 'RAMPZ',
        0x3D: 'SPL',
        0x3E: 'SPH',
        0x3F: 'SREG'
    }

    INTERRUPT_VECTORS = [
        'RESET_vect',
        'INT0_vect',
        'INT1_vect',
        'INT2_vect',
        'INT3_vect',
        'INT4_vect',
        'INT5_vect',
        'INT6_vect',
        'INT7_vect'
        'TIMER2_COMP_vect',
        'TIMER2_OVF_vect',
        'TIMER1_CAPT_vect',
        'TIMER1_COMPA_vect',
        'TIMER1_COMPB_vect',
        'TIMER1_COMPC_vect',
        'TIMER1_OVF_vect',
        'TIMER0_COMP_vect',
        'TIMER0_OVF_vect',
        'CANIT_vect',
        'OVRIT_vect',
        'SPI_STC_vect',
        'USART0_RX_vect',
        'USART0_UDRE_vect',
        'USART0_TX_vect',
        'ANALOG_COMP_vect',
        'ADC_vect',
        'EE_READY_vect',
        'TIMER3_CAPT_vect',
        'TIMER3_COMPA_vect',
        'TIMER3_COMPB_vect',
        'TIMER3_COMPC_vect',
        'TIMER3_OVF_vect',
        'USART1_RX_vect',
        'USART1_UDRE_vect',
        'USART1_TX_vect'
        'TWI_vect',
        'SPM_READY_vect'
    ]

    EXTENDED_IO_REGISTERS = {
        0x60: 'WDTCR',
        0x61: 'CLKPR',

        0x66: 'OSCCAL',

        0x69: 'EICRA',
        0x6A: 'EICRB',

        0x6E: 'TIMSK0',
        0x6F: 'TIMSK1',
        0x70: 'TIMSK2',
        0x71: 'TIMSK3',

        0x74: 'XMCRA',
        0x75: 'XMCRB',

        0x78: 'ADCL',
        0x79: 'ADCH',
        0x7A: 'ADCSRA',
        0x7B: 'ADCSRB',
        0x7C: 'ADMUX',

        0x7E: 'DIDR0',
        0x7F: 'DIDR1',
        0x80: 'TCCR1A',
        0x81: 'TCCR1B',
        0x82: 'TCCR1C',

        0x84: 'TCNT1L',
        0x85: 'TCNT1H',
        0x86: 'ICR1L',
        0x87: 'ICR1H',
        0x88: 'OCR1AL',
        0x89: 'OCR1AH',
        0x8A: 'OCR1BL',
        0x8B: 'OCR1BH',
        0x8C: 'OCR1CL',
        0x8D: 'OCR1CH',

        0x90: 'TCCR3A',
        0x91: 'TCCR3B',
        0x92: 'TCCR3C',

        0x94: 'TCNT3L',
        0x95: 'TCNT3H',
        0x96: 'ICR3L',
        0x97: 'ICR3H',
        0x98: 'OCR3AL',
        0x99: 'OCR3AH',
        0x9A: 'OCR3BL',
        0x9B: 'OCR3BH',
        0x9C: 'OCR3CL',
        0x9D: 'OCR3CH',

        0xB0: 'TCCR2A',

        0xB2: 'TCNT2',
        0xB3: 'OCR2A',

        0xB6: 'ASSR',

        0xB8: 'TWBR',
        0xB9: 'TWSR',
        0xBA: 'TWAR',
        0xBB: 'TWDR',
        0xBC: 'TWCR',

        0xC0: 'UCSR0A',
        0xC1: 'UCSR0B',
        0xC2: 'UCSR0C',
        0xC4: 'UBRR0L',
        0xC5: 'UBRR0H',
        0xC6: 'UDR0',

        0xC8: 'UCSR1A',
        0xC9: 'UCSR1B',
        0xCA: 'UCSR1C',

        0xCC: 'UBRR1L',
        0xCD: 'UBBR1H',
        0xCE: 'UDR1',

        0xD8: 'CANGCON',
        0xD9: 'CANGSTA',
        0xDA: 'CANGIT',
        0xDB: 'CANGIE',
        0xDC: 'CANGEN2',
        0xDD: 'CANGEN1',
        0xDE: 'CANIE2',
        0xDF: 'CANIE1',
        0xE0: 'CANSIT2',
        0xE1: 'CANSIT1',
        0xE2: 'CANBT1',
        0xE3: 'CANBT2',
        0xE4: 'CANBT3',
        0xE5: 'CANTCON',
        0xE6: 'CANTIML',
        0xE7: 'CANTIMH',
        0xE8: 'CANTTCL',
        0xE9: 'CANTTCH',
        0xEA: 'CANTEC',
        0xEB: 'CANREC',
        0xEC: 'CANHPMOB',
        0xED: 'CANPAGE',
        0xEE: 'CANSTMOB',
        0xEF: 'CANCDMOB',
        0xF0: 'CANIDT4',
        0xF1: 'CANIDT3',
        0xF2: 'CANIDT2',
        0xF3: 'CANIDT1',
        0xF4: 'CANIDM4',
        0xF5: 'CANIDM3',
        0xF6: 'CANIDM2',
        0xF7: 'CANIDM1',
        0xF8: 'CANSTML',
        0xF9: 'CANSTMH',
        0xFA: 'CANMSG',
    }

    @staticmethod
    def description():
        return "AT90CAN64"

    @staticmethod
    def identifier():
        return __class__.__name__
