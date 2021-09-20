// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFront::Distribution
 */
export class Distribution extends pulumi.CustomResource {
    /**
     * Get an existing Distribution resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Distribution {
        return new Distribution(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudfront:Distribution';

    /**
     * Returns true if the given object is an instance of Distribution.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Distribution {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Distribution.__pulumiType;
    }

    public readonly distributionConfig!: pulumi.Output<outputs.cloudfront.DistributionDistributionConfig>;
    public /*out*/ readonly domainName!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.cloudfront.DistributionTag[] | undefined>;

    /**
     * Create a Distribution resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DistributionArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.distributionConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'distributionConfig'");
            }
            inputs["distributionConfig"] = args ? args.distributionConfig : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["domainName"] = undefined /*out*/;
        } else {
            inputs["distributionConfig"] = undefined /*out*/;
            inputs["domainName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Distribution.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Distribution resource.
 */
export interface DistributionArgs {
    distributionConfig: pulumi.Input<inputs.cloudfront.DistributionDistributionConfigArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.cloudfront.DistributionTagArgs>[]>;
}
