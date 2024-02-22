// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Config::ConfigurationAggregator
 */
export class ConfigurationAggregator extends pulumi.CustomResource {
    /**
     * Get an existing ConfigurationAggregator resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConfigurationAggregator {
        return new ConfigurationAggregator(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:configuration:ConfigurationAggregator';

    /**
     * Returns true if the given object is an instance of ConfigurationAggregator.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfigurationAggregator {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfigurationAggregator.__pulumiType;
    }

    public readonly accountAggregationSources!: pulumi.Output<outputs.configuration.ConfigurationAggregatorAccountAggregationSource[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the aggregator.
     */
    public /*out*/ readonly configurationAggregatorArn!: pulumi.Output<string>;
    /**
     * The name of the aggregator.
     */
    public readonly configurationAggregatorName!: pulumi.Output<string | undefined>;
    public readonly organizationAggregationSource!: pulumi.Output<outputs.configuration.ConfigurationAggregatorOrganizationAggregationSource | undefined>;
    /**
     * The tags for the configuration aggregator.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a ConfigurationAggregator resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ConfigurationAggregatorArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["accountAggregationSources"] = args ? args.accountAggregationSources : undefined;
            resourceInputs["configurationAggregatorName"] = args ? args.configurationAggregatorName : undefined;
            resourceInputs["organizationAggregationSource"] = args ? args.organizationAggregationSource : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["configurationAggregatorArn"] = undefined /*out*/;
        } else {
            resourceInputs["accountAggregationSources"] = undefined /*out*/;
            resourceInputs["configurationAggregatorArn"] = undefined /*out*/;
            resourceInputs["configurationAggregatorName"] = undefined /*out*/;
            resourceInputs["organizationAggregationSource"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["configurationAggregatorName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConfigurationAggregator.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConfigurationAggregator resource.
 */
export interface ConfigurationAggregatorArgs {
    accountAggregationSources?: pulumi.Input<pulumi.Input<inputs.configuration.ConfigurationAggregatorAccountAggregationSourceArgs>[]>;
    /**
     * The name of the aggregator.
     */
    configurationAggregatorName?: pulumi.Input<string>;
    organizationAggregationSource?: pulumi.Input<inputs.configuration.ConfigurationAggregatorOrganizationAggregationSourceArgs>;
    /**
     * The tags for the configuration aggregator.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
