# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def get_config_fields(params):
    return {
        'pop_size': {
            'label': 'Population size (initial or fixed)',
            'value': params['pop_size'],
            'type': {
                'id': 'number',
                'min': 2,
                'max': 100000,
                'step': 1,
            },
            'help': 'This is the number of reproducing adults, after selection. This number is normally kept constant, except when fertility is insufficient to allow replacement, or when population growth is specified below. For smaller computer systems such as PCs, population size must remain small (100-5000) or the program will run out of memory. Population sizes smaller than 1000 can be strongly affected by inbreeding and drift.',
        },
        'num_generations': {
            'label': 'Generations',
            'value': params['num_generations'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'The number of generations the program should run. If there are too many generations specified, smaller computers will run out of memory because of the accumulation of large numbers of mutations, and the experiment will terminate prematurely. This problem can be mitigated by tracking only the larger-effect mutations (see advanced computation parameters).  The program also terminates prematurely if fitness reaches a specified extinction threshold (default = 0.0) or if the population size shrinks to just one individual. In the special case of pop_growth_model==exponential, this value can be 0 which indicates the run should continue until max_pop_size is reached.',
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
            'help': 'This is the average number of new mutations per individual. In humans, this number is believed to be approximately 100. The mutation rate can be adjusted to be proportional to the size of the functional genome. Thus if only 10% of the human genome actually functions (assuming the rest to be biologically inert), or if only 10% of the genome is modeled (as is the default), then the biologically relevant mutation rate would be just 10. Rates of less than 1 new mutation per individual are allowed—including zero. The human value is approximately 10 new mutations per individual per generation.',
        },
        'mutn_rate_model': {
            'label': 'Mutation rate model',
            'value': params['mutn_rate_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('fixed', 'Fixed'),
                    ('poisson', 'Poisson (default)'),
                ],
            },
            'help': 'Choices: "poisson" - mutn_rate is determined by a poisson distribution, or "fixed" - mutn_rate is rounded to the nearest int',
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
            'help': 'While some sources suggest this number might be as high as 1:1000, most sources suggest it is more realistically about 1:1,000,000. For studying the accumulation of only deleterious or only beneficial mutations, the fraction of beneficials can be set to zero or 1.',
        },
        'fraction_neutral': {
            'label': 'Fraction of the total number of mutations that are perfectly neutral',
            'value': params['fraction_neutral'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 1,
                'step': 'any',
            },
            'help': 'It is not clear that any mutations are perfectly neutral, but in the past it has often been claimed that most of the human genome is non-function “junk DNA”, and that mutations in these regions are truly neutral. For the human default, we allow (but do not believe) that 90% of the genome is junk DNA, and so 90% of all human mutations have absolutely no biological effect. Because of the computational cost of tracking so many neutral mutations we specify zero neutrals be simulated, and discount the genome size so it only reflects non-neutral mutations.',
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
                    ('weibull', 'Weibull (default)'),
                ],
            },
            'help': 'Choices: "weibull" - the fitness effect of each mutation is determined by the Weibull distribution, "fixed" - use fixed values for mutation fitness effect as set in uniform_fitness_effect_*, or "uniform" - even distribution between 0 and uniform_fitness_effect_* as max.',
        },
        'uniform_fitness_effect_del': {
            'label': 'For Fixed: effect for each deleterious mutation',
            'value': params['uniform_fitness_effect_del'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 0.1,
                'step': 'any',
            },
            'help': 'Used for fitness_effect_model=fixed. Each deleterious mutation should have this fitness effect.',
        },
        'uniform_fitness_effect_fav': {
            'label': 'For Fixed: effect for each beneficial mutation',
            'value': params['uniform_fitness_effect_fav'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 0.1,
                'step': 'any',
            },
            'help': 'Used for fitness_effect_model=fixed. Each beneficial mutation should have this fitness effect.',
        },
        'high_impact_mutn_fraction': {
            'label': 'Fraction of deleterious mutations with “major effect”',
            'value': params['high_impact_mutn_fraction'],
            'type': {
                'id': 'number',
                'min': 0.000000001,
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
            'help': 'It is widely believed that recessive mutations are not completely silent in the heterozygous condition, but are still expressed at some low level. Although the co-dominance value is 0.5 expression, a reasonable setting would be 0.05.',
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
            'help': 'It is widely believed that dominant mutations are not completely dominant in the heterozygous condition, but are only expressed only at some very high level. Although the co-dominance value is 0.5, a reasonable setting would be 0.95.',
        },
        'selection_model': {
            'label': 'Selection model',
            'value': params['selection_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('fulltrunc', 'Full truncation'),
                    ('ups', 'Unrestricted probability selection'),
                    ('spps', 'Strict proportionality probability selection (default)'),
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
            'help': 'Because a large part of phenotypic performance is affected by an individual’s circumstances (the “environment”), selection in nature is less effective than would be predicted simply from genotypic fitness values. Non-heritable environmental effects on phenotypic performance must be modeled realistically. A heritability value of 0.2 implies that on average, only 20% of an individual’s phenotypic performance is passed on to the next generation, with the rest being due to non-heritable factors. For a very general character such as reproductive fitness, 0.2 is an extremely generous heritability value. In most field contexts, it is in fact usually lower than this, typically being below the limit of detection.',
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
            'help': 'If a population’s fitness is increasing or declining, heritability (as calculated in the normal way), tends to scale with fitness, and so the implied “environmental noise” diminishes or increases as fitness diminishes or increases. This seems counter-intuitive. Also, with truncation selection, phenotypic variance becomes un-naturally small. For these reasons, it is desirable to model a component of environmental noise that does not scale with fitness variation. The units for this non-scaling noise parameter are based upon standard deviations from the initial fitness of 1.0. For simplicity, a reasonable value is 0.05, but reasonable values probably exceed 0.01 and might exceed 0.1.',
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
            'help': 'This is the number of offspring per reproducing individual. When population size is constant, this variable defines the maximum amount of selection. There must be an average of at least one offspring per individual (after the selection process) for the population to maintain its size and avoid rapid extinction. Except where random death is considered, the entire surplus population is removed based upon phenotypic selection. The typical value for humans is two offspring per selected individual (or four offspring per reproducing female).',
        },
        'num_offspring_model': {
            'label': 'Num offspring model',
            'value': params['num_offspring_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('uniform', 'Uniform'),
                    ('fixed', 'Fixed (default)'),
                ],
            },
            'help': 'Choices: "fixed" - reproductive_rate rounded to the nearest integer, or "uniform" - an even distribution such that the mean is reproductive_rate',
        },
        'crossover_model': {
            'label': 'Crossover model',
            'value': params['crossover_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('none', 'None'),
                    ('partial', 'Partial (default)'),
                    ('full', 'Full'),
                ],
            },
            'help': 'Choices: "partial" - mean_num_crossovers per chromosome pair, "none" - no crossover, or "full" - each LB has a 50/50 chance of coming from dad or mom',
        },
        'mean_num_crossovers': {
            'label': 'For Partial: Mean crossovers per chromosome pair',
            'value': params['mean_num_crossovers'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100,
                'step': 1,
            },
            'help': 'Used only for crossover_model=partial. The average number of crossovers per chromosome PAIR during Meiosis 1 Metaphase.',
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
            'help': 'The number of linkage blocks is evenly distributed over a user-specified haploid number of chromosomes (default=23).',
        },
        'num_linkage_subunits': {
            'label': 'Number of linkage subunits per individual',
            'value': params['num_linkage_subunits'],
            'type': {
                'id': 'number',
                'min': 1,
                'max': 100000,
                'step': 1,
            },
            'help': 'The number of linkage blocks. The number of linkage blocks should be an integer multiple of the number of chromosome (e.g. the default value of 989 is 43 times the default 23 chromosomes).',
        },
        'num_contrasting_alleles': {
            'label': 'Number of initial contrasting alleles per individual',
            'value': params['num_contrasting_alleles'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'Number of initial contrasting alleles (pairs) given to each individual. Used to start the population with pre-existing diversity.',
        },
        'initial_alleles_pop_frac': {
            'label': 'Fraction of the population that should have initial alleles',
            'value': params['initial_alleles_pop_frac'],
            'type': {
                'id': 'number',
                'min': 0.0,
                'max': 1.0,
                'step': 'any',
            },
            'help': 'Used along with num_contrasting_alleles to set the fraction of the initial population that should have num_contrasting_alleles alleles',
        },
        'max_total_fitness_increase': {
            'label': 'The total fitness effect of all of the favorable initial alleles in an individual',
            'value': params['max_total_fitness_increase'],
            'type': {
                'id': 'number',
                'min': 0.0,
                'max': 1.0,
                'step': 'any',
            },
            'help': 'Used along with num_contrasting_alleles to set the total fitness effect of all of the favorable initial alleles in an individual.',
        },
        'pop_growth_model': {
            'label': 'Population growth model',
            'value': params['pop_growth_model'],
            'type': {
                'id': 'select',
                'choices': [
                    ('none', 'None (default)'),
                    ('exponential', 'Exponential'),
                    ('capacity', 'Carrying capacity'),
                    ('founders', 'Founders effect'),
                ],
            },
            'help': 'Choices: "none" - no population growth, "exponential" - exponential growth model, "capacity" - carrying-capacity model, "founders" - founders effect',
        },
        'pop_growth_rate': {
            'label': 'Population growth rate each generation',
            'value': params['pop_growth_rate'],
            'type': {
                'id': 'number',
                'min': 0.0,
                'max': 10.0,
                'step': 'any',
            },
            'help': 'Population growth rate each generation (e.g. 1.05 is 5% increase). Used for pop_growth_model==Exponential, Carrying capacity, and Founders effect.',
        },
        'pop_growth_rate2': {
            'label': 'For Founders: Population growth rate after the bottleneck',
            'value': params['pop_growth_rate2'],
            'type': {
                'id': 'number',
                'min': 0.0,
                'max': 10.0,
                'step': 'any',
            },
            'help': 'Population growth rate after the population bottleneck. Used for pop_growth_model==Founders effect.',
        },
        'max_pop_size': {
            'label': 'For Exponential: Maximum population size',
            'value': params['max_pop_size'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'The run will stop when this population size is reached or num_generations is reached, whichever comes first. Set to 0 for no max. Used for pop_growth_model==exponential.',
        },
        'carrying_capacity': {
            'label': 'Population carrying capacity',
            'value': params['carrying_capacity'],
            'type': {
                'id': 'number',
                'min': 10,
                'max': 100000,
                'step': 1,
            },
            'help': 'The limit that the population size should approach. Used for pop_growth_model==Carrying capacity and Founders effect.',
            'more_help_url': 'https://en.wikipedia.org/wiki/Carrying_capacity',
        },
        'bottleneck_generation': {
            'label': 'Generation number of a population bottleneck',
            'value': params['bottleneck_generation'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'The generation number at which the population size bottleneck should start. Use 0 for no bottleneck. Currently only used for pop_growth_model==founders',
        },
        'bottleneck_pop_size': {
            'label': 'The population size during the bottleneck',
            'value': params['bottleneck_pop_size'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
        },
        'num_bottleneck_generations': {
            'label': 'The number of generations the bottleneck should last',
            'value': params['num_bottleneck_generations'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
        },
        'tracking_threshold': {
            'label': 'Do not track mutations below this fitness effect',
            'value': params['tracking_threshold'],
            'type': {
                'id': 'number',
                'min': 0.0,
                'max': 10.0,
                'step': 'any',
            },
            'help': 'Below this fitness effect value, near neutral mutations will be pooled into the cumulative fitness of the LB, instead of tracked individually. This saves on memory and computation time, but some stats will not be available. This value is automatically set to a high value if allele output is not requested, because there is no benefit to tracking in that case.',
        },
        'track_neutrals': {
            'label': 'Track neutral mutations',
            'value': params['track_neutrals'],
            'type': {
                'id': 'boolean',
            },
            'help': 'Checking this box will cause Mendel to track neutral mutations as long as tracking_threshold is also set to 0.0. This button must be checked if neutral mutations are to be simulated.',
        },
        'num_threads': {
            'label': 'Number of CPUs to use for the simulation',
            'value': params['num_threads'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'The number of concurrent CPU threads that should be used in the simulation. If this is set to 0 (recommended) it will automatically use all available CPUs.',
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
        'plot_allele_gens': {
            'label': 'Plot alleles every n generations',
            'value': params['plot_allele_gens'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'A value of 0 means only plot alleles for the last generation.',
        },
        'omit_first_allele_bin': {
            'label': 'Omit the 1st allele bin',
            'value': params['omit_first_allele_bin'],
            'type': {
                'id': 'boolean',
            },
            'help': 'If checked, do not output the 0-1% allele bin for allele plots. This is consistent with the way most geneticists plot this data.',
        },
        'verbosity': {
            'label': 'The verbosity of the output',
            'value': params['verbosity'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'A value of 1 is recommended. Higher values will output more information, but will also take longer to gather.',
        },
        'force_gc': {
            'label': 'Force system garbage collection each generation',
            'value': params['force_gc'],
            'type': {
                'id': 'boolean',
            },
            'help': 'Check this box to explicitly run Go garbage collection after mating each generation. (Otherwise Go decides when to run gargage collection.) Setting this can cut memory usage, sometimes as much as 40%, but it also increases the run time.',
        },
        'allele_count_gc_interval': {
            'label': 'Run Go garbage collection during allele counting after this %',
            'value': params['allele_count_gc_interval'],
            'type': {
                'id': 'number',
                'min': 0,
                'max': 100000,
                'step': 1,
            },
            'help': 'if 0 < n < 100 explicitly call Go garbage collection after counting this percent of individuals (with a min bound of 100 individuals and max bound of 500), or if n >= 100 call GC after counting alleles from this many individuals. This helps memory not balloon right at the end of a long run, but will take a little longer.',
        },
        'reuse_populations': {
            'label': 'Reuse internal code objects',
            'value': params['reuse_populations'],
            'type': {
                'id': 'boolean',
            },
            'help': 'Check this box to have the code explicitly reuse internal objects. The will increase performance around 20% (depending on parameters), but will more than double the amount of memory used. This will be forced to false if population growth is specified (because that combination is not supported yet).',
        },
        'files_to_output_fit': {
            'label': 'mendel.fit',
            'value': True,
            'type': {
                'id': 'boolean',
            },
            'help': 'This contains data needed for the "Fitness History" plot.',
        },
        'files_to_output_hst': {
            'label': 'mendel.hst',
            'value': True,
            'type': {
                'id': 'boolean',
            },
            'help': 'This contains data needed for the "Average Mutations/Individual" plot.',
        },
        'files_to_output_allele_bins': {
            'label': 'allele-bins/',
            'value': True,
            'type': {
                'id': 'boolean',
            },
            'help': 'This contains data needed for the "SNP Frequencies" and "Minor Allele Frequencies" plots.',
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
                {'id': 'genome_size'},
                {'id': 'mutn_rate_model'},
                {'id': 'frac_fav_mutn'},
                {'id': 'fraction_neutral'},
                {'id': 'fitness_effect_model',
                    'children': [
                        {'id': 'uniform_fitness_effect_del'},
                        {'id': 'uniform_fitness_effect_fav'},
                    ],
                },
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
                {'id': 'num_contrasting_alleles',
                    'children': [
                        {'id': 'initial_alleles_pop_frac'},
                        {'id': 'max_total_fitness_increase'},
                    ],
                },
                {'id': 'pop_growth_model',
                    'children': [
                        {'id': 'pop_growth_rate'},
                        {'id': 'pop_growth_rate2'},
                        {'id': 'max_pop_size'},
                        {'id': 'carrying_capacity'},
                    ],
                },
                {'id': 'bottleneck_generation',
                    'children': [
                        {'id': 'bottleneck_pop_size'},
                        {'id': 'num_bottleneck_generations'},
                    ],
                },
            ],
        },
        {
            'id': 'output_files',
            'title': 'Output Files',
            'fields': [
                {'id': 'files_to_output_fit'},
                {'id': 'files_to_output_hst'},
                {'id': 'files_to_output_allele_bins'},
            ],
        },
        {
            'id': 'computation',
            'title': 'Computation',
            'fields': [
                {'id': 'tracking_threshold'},
                {'id': 'track_neutrals'},
                {'id': 'plot_allele_gens'},
                {'id': 'omit_first_allele_bin'},
                {'id': 'random_number_seed'},
                {'id': 'verbosity'},
                {'id': 'num_threads'},
                {'id': 'force_gc'},
                {'id': 'allele_count_gc_interval'},
                {'id': 'reuse_populations'},
            ],
        },
    ]
