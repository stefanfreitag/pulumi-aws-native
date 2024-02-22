// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::TrafficMirrorFilter
 *
 * @deprecated TrafficMirrorFilter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class TrafficMirrorFilter extends pulumi.CustomResource {
    /**
     * Get an existing TrafficMirrorFilter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TrafficMirrorFilter {
        pulumi.log.warn("TrafficMirrorFilter is deprecated: TrafficMirrorFilter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new TrafficMirrorFilter(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:TrafficMirrorFilter';

    /**
     * Returns true if the given object is an instance of TrafficMirrorFilter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TrafficMirrorFilter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TrafficMirrorFilter.__pulumiType;
    }

    public readonly description!: pulumi.Output<string | undefined>;
    public readonly networkServices!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a TrafficMirrorFilter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated TrafficMirrorFilter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: TrafficMirrorFilterArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("TrafficMirrorFilter is deprecated: TrafficMirrorFilter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["networkServices"] = args ? args.networkServices : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["networkServices"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["description"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(TrafficMirrorFilter.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a TrafficMirrorFilter resource.
 */
export interface TrafficMirrorFilterArgs {
    description?: pulumi.Input<string>;
    networkServices?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
