# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def get_config_fields(params):
    return {
        'pop_size': {
            'label': 'Population size (per subpopulation)',
            'value': params['pop_size'],
            'type': {
                'id': 'number',
                'min': 2,
                'max': 100000,
                'step': 1,
            },
            'help': 'This is the number of reproducing adults, after selection. For parallel runs, this is the population size of each sub-population. This number is normally kept constant, except where fertility is insufficient to allow replacement, or where certain advanced parameters are used. For smaller computer systems such as PCs, population size must remain small (100-1000) or the program will quickly run out of memory. The default value is 1,000, since population sizes smaller than this can be strongly affected by inbreeding and drift. We find increasing population size beyond 1000 results in rapidly diminishing selective benefit.',
        },
        'num_generations': {
            'label': 'Generations',
            'value': params['num_generations'],
            'type': {
                'id': 'number',
                'min': 1,
                'max': 100000,
                'step': 1,
            },
            'help': 'The number of generations the program should run. The default is 500 generations. If there are too many generations specified, smaller computers will run out of memory because of the accumulation of large numbers of mutations, and the experiment will terminate prematurely. This problem can be mitigated by tracking only the larger-effect mutations (see advanced computation parameters).  The program also terminates prematurely if fitness reaches a specified extinction threshold (default = 0.0) or if the population size shrinks to just one individual.',
        },
        'mutn_rate': {
            'label': 'Total non-neutral mutation rate (per individual per generation)',
            'value': params['mutn_rate'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1000,
                'step': 'any',
            },
            'help': 'This is the average number of new mutations per individual. In humans, this number is believed to be approximately 100. The mutation rate can be adjusted to be proportional to the size of the functional genome. Thus if only 10% of the human genome actually functions (assuming the rest to be biologically inert), then the biologically relevant mutation rate would be just 10. Rates of less than 1 new mutation per individual are allowed—including zero. The human default value is 10 new mutations per individual per generation.',
        },
        'mutn_rate_model': {
            'label': 'Mutation rate model',
            'value': params['mutn_rate_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('fixed', 'Fixed'),
                    ('poisson', 'Poisson'),
                ],
            },
        },
        'frac_fav_mutn': {
            'label': 'Beneficial/deleterious ratio within non-neutral mutations',
            'value': params['frac_fav_mutn'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'While some sources suggest this number might be as high as 1:1000, most sources suggest it is more realistically about 1:1,000,000. The default setting is 1:10,000. For studying the accumulation of only deleterious or only beneficial mutations, the number of beneficials can be set to zero or one.',
        },
        'fraction_neutral': {
            'label': 'Fraction of genome which is non-functional (junk)',
            'value': params['fraction_neutral'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'It is not clear that any mutations are perfectly neutral, but in the past it has often been claimed that most of the human genome is non-function “junk DNA”, and that mutations in these regions are truly neutral. For the human default, we allow (but do not believe) that 90% of the genome is junk DNA, and so 90% of all human mutations have absolutely no biological effect. Because of the computational cost of tracking so many neutral mutations we specify zero neutrals be simulated, and discount the mutation rate so it only reflects non-neutral mutations (see above).',
            'more_help_url': '/static/apps/mendel/help.html#fmun',
        },
        'genome_size': {
            'label': 'Functional genome size',
            'value': params['genome_size'],
            'type': {
                'id': 'number',
                'min': 100,
                'max': 1e11,
                'step': 1,
            },
            'help': 'The distribution of deleterious mutational effects must in some way be adjusted to account for genome size. An approximate yet reasonable means for doing this is to define the minimal mutational effect as being 1 divided by the functional haploid genome size. The result of this adjustment is that smaller genomes have “flatter” distributions of deleterious mutations, while larger genomes have “steeper” distribution curves. Because we consider all entirely neutral mutations separately, we only consider the size of the functional genome, so we choose the default genome size to be 300 million (10% of the actual human genome size).',
            'more_help_url': '/static/apps/mendel/help.html#hgs',
        },
        'fitness_effect_model': {
            'label': 'Fitness effect model',
            'value': params['fitness_effect_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('fixed', 'Fixed'),
                    ('uniform', 'Uniform'),
                    ('weibull', 'Weibull'),
                ],
            },
        },
        'uniform_fitness_effect_del': {
            'label': 'Equal effect for each deleterious mutation',
            'value': params['uniform_fitness_effect_del'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 0.1,
                'step': 'any',
            },
        },
        'uniform_fitness_effect_fav': {
            'label': 'Equal effect for each beneficial mutation',
            'value': params['uniform_fitness_effect_fav'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 0.1,
                'step': 'any',
            },
        },
        'high_impact_mutn_fraction': {
            'label': 'Fraction of deleterious mutations with “major effect”',
            'value': params['high_impact_mutn_fraction'],
            'type': {
                'id': 'number',
                'min': 0.0001,
                'max': 0.9,
                'step': 'any',
            },
            'help': 'Most mutations have an effect on fitness that is too small to measure directly. However, mutations will have measurable effects in the far “tail” of the mutation distribution curve. By utilizing the frequency and distribution of “measurable” mutation effects, one can constrain the most significant portion of the distribution curve as it relates to the selection process. For most species, there may not yet be enough data, even for the major mutations, to accurately model the exact distribution of mutations. When such data is not yet available, we are forced to simply estimate, to the best of our ability and based on data from other organisms, the fraction of “major mutations”.  The human default is 0.001.',
        },
        'high_impact_mutn_threshold': {
            'label': 'Minimum deleterious effect defined as “major”',
            'value': params['high_impact_mutn_threshold'],
            'type': {
                'id': 'number',
                'min': 0.0001,
                'max': 0.9,
                'step': 'any',
            },
            'help': 'A somewhat arbitrary level must be selected for defining what constitutes a “measurable”, or “major”, mutation effect. MENDEL uses a default value for this cut-off of 0.10. This is because under realistic clinical conditions, it is questionable that we can reliably measure a single mutation’s fitness effect when it changes fitness by less than 10%.',
        },
        'max_fav_fitness_gain': {
            'label': 'Maximum beneficial fitness effect',
            'value': params['max_fav_fitness_gain'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'A realistic upper limit must be placed upon beneficial mutations. This is because a single nucleotide change can expand total biological functionality of an organism only to a limited degree. The larger the genome and the greater the total genomic information, the less a single nucleotide is likely to increase the total. Researchers must make a judgment for themselves of what is a reasonable maximal value for a single base change. The MENDEL default value for this limit is 0.01. This limit implies that a single point mutation can increase total biological functionality by as much as 1%.',
            'more_help_url': '/static/apps/mendel/help.html#rdbm',
        },
        'fraction_recessive': {
            'label': 'Fraction recessive (rest dominant)',
            'value': params['fraction_recessive'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'This parameter simply specifies the percentage of mutations that are recessive. If set to 0.8, then 80% of mutations are recessive, so the remaining 20% will automatically be made dominant.',
        },
        'recessive_hetero_expression': {
            'label': 'Expression of recessive mutations (in heterozygote)',
            'value': params['recessive_hetero_expression'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 0.5,
                'step': 'any',
            },
            'help': 'It is widely believed that recessive mutations are not completely silent in the heterozygous condition, but are still expressed at some low level. Although the co-dominance default is 0.5 expression, a reasonable setting would be 0.05.',
        },
        'dominant_hetero_expression': {
            'label': 'Expression of dominant mutations (in heterozygote)',
            'value': params['dominant_hetero_expression'],
            'type': {
                'id': 'number',
                'min': 0.5,
                'max': 1,
                'step': 'any',
            },
            'help': 'It is widely believed that dominant mutations are not completely dominant in the heterozygous condition, but are only expressed only at some very high level. Although the co-dominance default is 0.5, a reasonable setting would be 0.95.',
        },
        'selection_model': {
            'label': 'Selection model',
            'value': params['selection_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('fulltrunc', 'Full truncation'),
                    ('ups', 'Unrestricted probability selection'),
                    ('spps', 'Strict proportionality probability selection'),
                    ('partialtrunc', 'Partial truncation selection'),
                ],
            },
        },
        'heritability': {
            'label': 'Heritability',
            'value': params['heritability'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'Because a large part of phenotypic performance is affected by an individual’s circumstances (the “environment”), selection in nature is less effective than would be predicted simply from genotypic fitness values. Non-heritable environmental effects on phenotypic performance must be modeled realistically. MENDEL’s default value for the heritability is 0.2. This implies that on average, only 20% of an individual’s phenotypic performance is passed on to the next generation, with the rest being due to non-heritable factors. For a very general character such as reproductive fitness, 0.2 is an extremely generous heritability value. In most field contexts, it is in fact usually lower than this, typically being below the limit of detection.',
        },
        'non_scaling_noise': {
            'label': 'Non-scaling noise',
            'value': params['non_scaling_noise'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'If a population’s fitness is increasing or declining, heritability (as calculated in the normal way), tends to scale with fitness, and so the implied “environmental noise” diminishes or increases as fitness diminishes or increases. This seems counter-intuitive. Also, with truncation selection, phenotypic variance becomes un-naturally small. For these reasons, it is desirable to model a component of environmental noise that does not scale with fitness variation. The units for this non-scaling noise parameter are based upon standard deviations from the initial fitness of 1.0. For simplicity, the default value is 0.05, but reasonable values probably exceed 0.01 and might exceed 0.1.',
            'more_help_url': '/static/apps/mendel/help.html#nsn',
        },
        'reproductive_rate': {
            'label': 'Reproductive rate',
            'value': params['reproductive_rate'],
            'type': {
                'id': 'number',
                'min': 1,
                'max': 25,
                'step': 1,
            },
            'help': 'This is the number of offspring per reproducing individual. Since population size in Mendel is usually constant, this variable defines the maximum amount of selection. There must be an average of at least one offspring per individual (after the selection process) for the population to maintain its size and avoid rapid extinction. Except where random death is considered, the entire surplus population is removed based upon phenotypic selection. The default value for humans is two offspring per selected individual (or four offspring per reproducing female).',
        },
        'num_offspring_model': {
            'label': 'Num offspring model',
            'value': params['num_offspring_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('uniform', 'Uniform'),
                    ('fixed', 'Fixed'),
                    ('fortran', 'Fortran'),
                ],
            },
        },
        'crossover_model': {
            'label': 'Crossover model',
            'value': params['crossover_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('none', 'None'),
                    ('partial', 'Partial'),
                    ('full', 'Full'),
                ],
            },
        },
        'mean_num_crossovers': {
            'label': 'Mean crossovers per chromosome pair',
            'value': params['mean_num_crossovers'],
            'type': {
                'id': 'number',
                'min': 2,
                'max': 100,
                'step': 1,
            },
        },
        'haploid_chromosome_number': {
            'label': 'Haploid chromosome number',
            'value': params['haploid_chromosome_number'],
            'type': {
                'id': 'number',
                'min': 1,
                'max': 100,
                'step': 1,
            },
            'help': 'The number of linkage blocks is evenly distributed over a user-specified haploid number of chromosomes (default=23).  If dynamic linkage is turned off, this number is not required and will be disabled.',
        },
        'num_linkage_subunits': {
            'label': 'Number of linkage subunits',
            'value': params['num_linkage_subunits'],
            'type': {
                'id': 'number',
                'min': 1,
                'max': 100000,
                'step': 1,
            },
            'help': 'Enter the number of linkage blocks. The number of linkage blocks should be an integer multiple of the number of chromosome (e.g. the default value of 989 is 43 times the default 23 chromosomes). MENDEL will automatically adjust to the nearest integer multiple (e.g. if you input 1000 and 23 chromosomes, MENDEL will use a value of 989).',
        },
        'track_neutrals': {
            'label': 'Track all mutations',
            'value': params['track_neutrals'],
            'type': {
                'id': 'boolean',
            },
            'help': 'Checking this box will set tracking threshold to zero, in which case all mutations will be tracked, including neutral mutations. This button must be checked if allele statistics are needed, or if neutral mutations are to be simulated.',
        },
        'random_number_seed': {
            'label': 'Random number generator (RNG) seed',
            'value': params['random_number_seed'],
            'type': {
                'id': 'number',
                'min': -9223372036854775808,
                'max': 9223372036854775807,
                'step': 1,
            },
            'help': 'At several stages within the MENDEL program, a random number generator is required. When an experiment needs to be independently replicated, the “random number seed” must be changed. If this is not done, the second experiment will be an exact duplicate of the earlier run.',
        },
    }

def get_config_tabs():
    return [
        {
            'id': 'basic',
            'title': 'Basic',
            'fields': [
                {'id': 'pop_size'},
                {'id': 'num_generations'},
            ],
        },
        {
            'id': 'mutations',
            'title': 'Mutations',
            'fields': [
                {'id': 'mutn_rate'},
                {'id': 'mutn_rate_model'},
                {'id': 'frac_fav_mutn'},
                {'id': 'fraction_neutral'},
                {'id': 'genome_size'},
                {'id': 'fitness_effect_model'},
                {'id': 'uniform_fitness_effect_del'},
                {'id': 'uniform_fitness_effect_fav'},
                {'id': 'high_impact_mutn_fraction'},
                {'id': 'high_impact_mutn_threshold'},
                {'id': 'max_fav_fitness_gain'},
                {'id': 'fraction_recessive'},
                {'id': 'recessive_hetero_expression'},
                {'id': 'dominant_hetero_expression'},
            ],
        },
        {
            'id': 'selection',
            'title': 'Selection',
            'fields': [
                {'id': 'selection_model'},
                {'id': 'heritability'},
                {'id': 'non_scaling_noise'},
            ],
        },
        {
            'id': 'population',
            'title': 'Population',
            'fields': [
                {'id': 'reproductive_rate'},
                {'id': 'num_offspring_model'},
                {'id': 'crossover_model',
                    'children': [
                        {'id': 'mean_num_crossovers'},
                    ],
                },
                {'id': 'haploid_chromosome_number'},
                {'id': 'num_linkage_subunits'},
            ],
        },
        {
            'id': 'computation',
            'title': 'Computation',
            'fields': [
                {'id': 'track_neutrals'},
                {'id': 'random_number_seed'},
            ],
        },
    ]