// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::Campaign
 *
 * @deprecated Campaign is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Campaign extends pulumi.CustomResource {
    /**
     * Get an existing Campaign resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Campaign {
        pulumi.log.warn("Campaign is deprecated: Campaign is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Campaign(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpoint:Campaign';

    /**
     * Returns true if the given object is an instance of Campaign.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Campaign {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Campaign.__pulumiType;
    }

    public readonly additionalTreatments!: pulumi.Output<outputs.pinpoint.CampaignWriteTreatmentResource[] | undefined>;
    public readonly applicationId!: pulumi.Output<string>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly campaignHook!: pulumi.Output<outputs.pinpoint.CampaignCampaignHook | undefined>;
    public /*out*/ readonly campaignId!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly holdoutPercent!: pulumi.Output<number | undefined>;
    public readonly isPaused!: pulumi.Output<boolean | undefined>;
    public readonly limits!: pulumi.Output<outputs.pinpoint.CampaignLimits | undefined>;
    public readonly messageConfiguration!: pulumi.Output<outputs.pinpoint.CampaignMessageConfiguration>;
    public readonly name!: pulumi.Output<string>;
    public readonly schedule!: pulumi.Output<outputs.pinpoint.CampaignSchedule>;
    public readonly segmentId!: pulumi.Output<string>;
    public readonly segmentVersion!: pulumi.Output<number | undefined>;
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly treatmentDescription!: pulumi.Output<string | undefined>;
    public readonly treatmentName!: pulumi.Output<string | undefined>;

    /**
     * Create a Campaign resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Campaign is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: CampaignArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Campaign is deprecated: Campaign is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.applicationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationId'");
            }
            if ((!args || args.messageConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'messageConfiguration'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.schedule === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schedule'");
            }
            if ((!args || args.segmentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'segmentId'");
            }
            inputs["additionalTreatments"] = args ? args.additionalTreatments : undefined;
            inputs["applicationId"] = args ? args.applicationId : undefined;
            inputs["campaignHook"] = args ? args.campaignHook : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["holdoutPercent"] = args ? args.holdoutPercent : undefined;
            inputs["isPaused"] = args ? args.isPaused : undefined;
            inputs["limits"] = args ? args.limits : undefined;
            inputs["messageConfiguration"] = args ? args.messageConfiguration : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
            inputs["segmentId"] = args ? args.segmentId : undefined;
            inputs["segmentVersion"] = args ? args.segmentVersion : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["treatmentDescription"] = args ? args.treatmentDescription : undefined;
            inputs["treatmentName"] = args ? args.treatmentName : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["campaignId"] = undefined /*out*/;
        } else {
            inputs["additionalTreatments"] = undefined /*out*/;
            inputs["applicationId"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["campaignHook"] = undefined /*out*/;
            inputs["campaignId"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["holdoutPercent"] = undefined /*out*/;
            inputs["isPaused"] = undefined /*out*/;
            inputs["limits"] = undefined /*out*/;
            inputs["messageConfiguration"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["schedule"] = undefined /*out*/;
            inputs["segmentId"] = undefined /*out*/;
            inputs["segmentVersion"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["treatmentDescription"] = undefined /*out*/;
            inputs["treatmentName"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Campaign.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Campaign resource.
 */
export interface CampaignArgs {
    additionalTreatments?: pulumi.Input<pulumi.Input<inputs.pinpoint.CampaignWriteTreatmentResourceArgs>[]>;
    applicationId: pulumi.Input<string>;
    campaignHook?: pulumi.Input<inputs.pinpoint.CampaignCampaignHookArgs>;
    description?: pulumi.Input<string>;
    holdoutPercent?: pulumi.Input<number>;
    isPaused?: pulumi.Input<boolean>;
    limits?: pulumi.Input<inputs.pinpoint.CampaignLimitsArgs>;
    messageConfiguration: pulumi.Input<inputs.pinpoint.CampaignMessageConfigurationArgs>;
    name: pulumi.Input<string>;
    schedule: pulumi.Input<inputs.pinpoint.CampaignScheduleArgs>;
    segmentId: pulumi.Input<string>;
    segmentVersion?: pulumi.Input<number>;
    tags?: any;
    treatmentDescription?: pulumi.Input<string>;
    treatmentName?: pulumi.Input<string>;
}
