// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Config::OrganizationConformancePack.
 */
export class OrganizationConformancePack extends pulumi.CustomResource {
    /**
     * Get an existing OrganizationConformancePack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): OrganizationConformancePack {
        return new OrganizationConformancePack(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:configuration:OrganizationConformancePack';

    /**
     * Returns true if the given object is an instance of OrganizationConformancePack.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrganizationConformancePack {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrganizationConformancePack.__pulumiType;
    }

    /**
     * A list of ConformancePackInputParameter objects.
     */
    public readonly conformancePackInputParameters!: pulumi.Output<outputs.configuration.OrganizationConformancePackConformancePackInputParameter[] | undefined>;
    /**
     * AWS Config stores intermediate files while processing conformance pack template.
     */
    public readonly deliveryS3Bucket!: pulumi.Output<string | undefined>;
    /**
     * The prefix for the delivery S3 bucket.
     */
    public readonly deliveryS3KeyPrefix!: pulumi.Output<string | undefined>;
    /**
     * A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.
     */
    public readonly excludedAccounts!: pulumi.Output<string[] | undefined>;
    /**
     * The name of the organization conformance pack.
     */
    public readonly organizationConformancePackName!: pulumi.Output<string>;
    /**
     * A string containing full conformance pack template body.
     */
    public readonly templateBody!: pulumi.Output<string | undefined>;
    /**
     * Location of file containing the template body.
     */
    public readonly templateS3Uri!: pulumi.Output<string | undefined>;

    /**
     * Create a OrganizationConformancePack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OrganizationConformancePackArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["conformancePackInputParameters"] = args ? args.conformancePackInputParameters : undefined;
            resourceInputs["deliveryS3Bucket"] = args ? args.deliveryS3Bucket : undefined;
            resourceInputs["deliveryS3KeyPrefix"] = args ? args.deliveryS3KeyPrefix : undefined;
            resourceInputs["excludedAccounts"] = args ? args.excludedAccounts : undefined;
            resourceInputs["organizationConformancePackName"] = args ? args.organizationConformancePackName : undefined;
            resourceInputs["templateBody"] = args ? args.templateBody : undefined;
            resourceInputs["templateS3Uri"] = args ? args.templateS3Uri : undefined;
        } else {
            resourceInputs["conformancePackInputParameters"] = undefined /*out*/;
            resourceInputs["deliveryS3Bucket"] = undefined /*out*/;
            resourceInputs["deliveryS3KeyPrefix"] = undefined /*out*/;
            resourceInputs["excludedAccounts"] = undefined /*out*/;
            resourceInputs["organizationConformancePackName"] = undefined /*out*/;
            resourceInputs["templateBody"] = undefined /*out*/;
            resourceInputs["templateS3Uri"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(OrganizationConformancePack.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a OrganizationConformancePack resource.
 */
export interface OrganizationConformancePackArgs {
    /**
     * A list of ConformancePackInputParameter objects.
     */
    conformancePackInputParameters?: pulumi.Input<pulumi.Input<inputs.configuration.OrganizationConformancePackConformancePackInputParameterArgs>[]>;
    /**
     * AWS Config stores intermediate files while processing conformance pack template.
     */
    deliveryS3Bucket?: pulumi.Input<string>;
    /**
     * The prefix for the delivery S3 bucket.
     */
    deliveryS3KeyPrefix?: pulumi.Input<string>;
    /**
     * A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.
     */
    excludedAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the organization conformance pack.
     */
    organizationConformancePackName?: pulumi.Input<string>;
    /**
     * A string containing full conformance pack template body.
     */
    templateBody?: pulumi.Input<string>;
    /**
     * Location of file containing the template body.
     */
    templateS3Uri?: pulumi.Input<string>;
}
