// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Config::AggregationAuthorization
 */
export class AggregationAuthorization extends pulumi.CustomResource {
    /**
     * Get an existing AggregationAuthorization resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AggregationAuthorization {
        return new AggregationAuthorization(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:configuration:AggregationAuthorization';

    /**
     * Returns true if the given object is an instance of AggregationAuthorization.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AggregationAuthorization {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AggregationAuthorization.__pulumiType;
    }

    /**
     * The ARN of the AggregationAuthorization.
     */
    public /*out*/ readonly aggregationAuthorizationArn!: pulumi.Output<string>;
    /**
     * The 12-digit account ID of the account authorized to aggregate data.
     */
    public readonly authorizedAccountId!: pulumi.Output<string>;
    /**
     * The region authorized to collect aggregated data.
     */
    public readonly authorizedAwsRegion!: pulumi.Output<string>;
    /**
     * The tags for the AggregationAuthorization.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a AggregationAuthorization resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AggregationAuthorizationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.authorizedAccountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'authorizedAccountId'");
            }
            if ((!args || args.authorizedAwsRegion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'authorizedAwsRegion'");
            }
            resourceInputs["authorizedAccountId"] = args ? args.authorizedAccountId : undefined;
            resourceInputs["authorizedAwsRegion"] = args ? args.authorizedAwsRegion : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["aggregationAuthorizationArn"] = undefined /*out*/;
        } else {
            resourceInputs["aggregationAuthorizationArn"] = undefined /*out*/;
            resourceInputs["authorizedAccountId"] = undefined /*out*/;
            resourceInputs["authorizedAwsRegion"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["authorizedAccountId", "authorizedAwsRegion"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AggregationAuthorization.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AggregationAuthorization resource.
 */
export interface AggregationAuthorizationArgs {
    /**
     * The 12-digit account ID of the account authorized to aggregate data.
     */
    authorizedAccountId: pulumi.Input<string>;
    /**
     * The region authorized to collect aggregated data.
     */
    authorizedAwsRegion: pulumi.Input<string>;
    /**
     * The tags for the AggregationAuthorization.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
