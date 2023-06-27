// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions
 */
export class AccessPoint extends pulumi.CustomResource {
    /**
     * Get an existing AccessPoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AccessPoint {
        return new AccessPoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:s3objectlambda:AccessPoint';

    /**
     * Returns true if the given object is an instance of AccessPoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessPoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessPoint.__pulumiType;
    }

    public /*out*/ readonly alias!: pulumi.Output<outputs.s3objectlambda.AccessPointAlias>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The date and time when the Object lambda Access Point was created.
     */
    public /*out*/ readonly creationDate!: pulumi.Output<string>;
    /**
     * The name you want to assign to this Object lambda Access Point.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
     */
    public readonly objectLambdaConfiguration!: pulumi.Output<outputs.s3objectlambda.AccessPointObjectLambdaConfiguration>;
    public /*out*/ readonly policyStatus!: pulumi.Output<outputs.s3objectlambda.AccessPointPolicyStatus>;
    /**
     * The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
     */
    public /*out*/ readonly publicAccessBlockConfiguration!: pulumi.Output<outputs.s3objectlambda.AccessPointPublicAccessBlockConfiguration>;

    /**
     * Create a AccessPoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessPointArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.objectLambdaConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'objectLambdaConfiguration'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["objectLambdaConfiguration"] = args ? args.objectLambdaConfiguration : undefined;
            resourceInputs["alias"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationDate"] = undefined /*out*/;
            resourceInputs["policyStatus"] = undefined /*out*/;
            resourceInputs["publicAccessBlockConfiguration"] = undefined /*out*/;
        } else {
            resourceInputs["alias"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationDate"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["objectLambdaConfiguration"] = undefined /*out*/;
            resourceInputs["policyStatus"] = undefined /*out*/;
            resourceInputs["publicAccessBlockConfiguration"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AccessPoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AccessPoint resource.
 */
export interface AccessPointArgs {
    /**
     * The name you want to assign to this Object lambda Access Point.
     */
    name?: pulumi.Input<string>;
    /**
     * The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
     */
    objectLambdaConfiguration: pulumi.Input<inputs.s3objectlambda.AccessPointObjectLambdaConfigurationArgs>;
}
