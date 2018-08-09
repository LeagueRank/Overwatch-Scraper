from .utils import parse_timespan, parse_percent


stats = {
    'hero': {
        'quickplay_timeplayed': {
            'parent_id': 'quickplay',
            'selector': 'overwatch.guid.0x0860000000000021',
            'value_parser': parse_timespan
        },
        'quickplay_gameswon': {
            'parent_id': 'quickplay',
            'selector': 'overwatch.guid.0x0860000000000039',
            'value_parser': int
        },
        'quickplay_accuracy': {
            'parent_id': 'quickplay',
            'selector': 'overwatch.guid.0x086000000000002F',
            'value_parser': parse_percent
        },
        'quickplay_kdratio': {
            'parent_id': 'quickplay',
            'selector': 'overwatch.guid.0x08600000000003D2',
            'value_parser': float
        },
        'quickplay_bestmultikill': {
            'parent_id': 'quickplay',
            'selector': 'overwatch.guid.0x0860000000000346',
            'value_parser': int
        },
        'quickplay_avgobjectivekills': {
            'parent_id': 'quickplay',
            'selector': 'overwatch.guid.0x086000000000039C',
            'value_parser': float
        },


        'competitive_timeplayed': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x0860000000000021',
            'value_parser': parse_timespan
        },
        'competitive_gameswon': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x0860000000000039',
            'value_parser': int
        },
        'competitive_accuracy': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x086000000000002F',
            'value_parser': parse_percent
        },
        'competitive_winrate': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x08600000000003D1',
            'value_parser': parse_percent
        },
        'competitive_kdratio': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x08600000000003D2',
            'value_parser': float
        },
        'competitive_bestmultikill': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x0860000000000346',
            'value_parser': int
        },
        'competitive_avgobjectivekills': {
            'parent_id': 'competitive',
            'selector': 'overwatch.guid.0x086000000000039C',
            'value_parser': float
        },
    }
}
