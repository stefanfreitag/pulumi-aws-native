// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EventSchemas::Discoverer
 *
 * @deprecated Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Discoverer extends pulumi.CustomResource {
    /**
     * Get an existing Discoverer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Discoverer {
        pulumi.log.warn("Discoverer is deprecated: Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Discoverer(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:eventschemas:Discoverer';

    /**
     * Returns true if the given object is an instance of Discoverer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Discoverer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Discoverer.__pulumiType;
    }

    public readonly crossAccount!: pulumi.Output<boolean | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly discovererArn!: pulumi.Output<string>;
    public /*out*/ readonly discovererId!: pulumi.Output<string>;
    public readonly sourceArn!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.eventschemas.DiscovererTagsEntry[] | undefined>;

    /**
     * Create a Discoverer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DiscovererArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Discoverer is deprecated: Discoverer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.sourceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceArn'");
            }
            resourceInputs["crossAccount"] = args ? args.crossAccount : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["sourceArn"] = args ? args.sourceArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["discovererArn"] = undefined /*out*/;
            resourceInputs["discovererId"] = undefined /*out*/;
        } else {
            resourceInputs["crossAccount"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["discovererArn"] = undefined /*out*/;
            resourceInputs["discovererId"] = undefined /*out*/;
            resourceInputs["sourceArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Discoverer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Discoverer resource.
 */
export interface DiscovererArgs {
    crossAccount?: pulumi.Input<boolean>;
    description?: pulumi.Input<string>;
    sourceArn: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.eventschemas.DiscovererTagsEntryArgs>[]>;
}
