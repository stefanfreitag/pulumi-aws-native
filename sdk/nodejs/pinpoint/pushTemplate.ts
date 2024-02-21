// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::PushTemplate
 *
 * @deprecated PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class PushTemplate extends pulumi.CustomResource {
    /**
     * Get an existing PushTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PushTemplate {
        pulumi.log.warn("PushTemplate is deprecated: PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new PushTemplate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpoint:PushTemplate';

    /**
     * Returns true if the given object is an instance of PushTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PushTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PushTemplate.__pulumiType;
    }

    public readonly adm!: pulumi.Output<outputs.pinpoint.PushTemplateAndroidPushNotificationTemplate | undefined>;
    public readonly apns!: pulumi.Output<outputs.pinpoint.PushTemplateApnsPushNotificationTemplate | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly baidu!: pulumi.Output<outputs.pinpoint.PushTemplateAndroidPushNotificationTemplate | undefined>;
    public readonly default!: pulumi.Output<outputs.pinpoint.PushTemplateDefaultPushNotificationTemplate | undefined>;
    public readonly defaultSubstitutions!: pulumi.Output<string | undefined>;
    public readonly gcm!: pulumi.Output<outputs.pinpoint.PushTemplateAndroidPushNotificationTemplate | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::PushTemplate` for more information about the expected schema for this property.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly templateDescription!: pulumi.Output<string | undefined>;
    public readonly templateName!: pulumi.Output<string>;

    /**
     * Create a PushTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: PushTemplateArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("PushTemplate is deprecated: PushTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.templateName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'templateName'");
            }
            resourceInputs["adm"] = args ? args.adm : undefined;
            resourceInputs["apns"] = args ? args.apns : undefined;
            resourceInputs["baidu"] = args ? args.baidu : undefined;
            resourceInputs["default"] = args ? args.default : undefined;
            resourceInputs["defaultSubstitutions"] = args ? args.defaultSubstitutions : undefined;
            resourceInputs["gcm"] = args ? args.gcm : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["templateDescription"] = args ? args.templateDescription : undefined;
            resourceInputs["templateName"] = args ? args.templateName : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["adm"] = undefined /*out*/;
            resourceInputs["apns"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["baidu"] = undefined /*out*/;
            resourceInputs["default"] = undefined /*out*/;
            resourceInputs["defaultSubstitutions"] = undefined /*out*/;
            resourceInputs["gcm"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["templateDescription"] = undefined /*out*/;
            resourceInputs["templateName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["templateName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(PushTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PushTemplate resource.
 */
export interface PushTemplateArgs {
    adm?: pulumi.Input<inputs.pinpoint.PushTemplateAndroidPushNotificationTemplateArgs>;
    apns?: pulumi.Input<inputs.pinpoint.PushTemplateApnsPushNotificationTemplateArgs>;
    baidu?: pulumi.Input<inputs.pinpoint.PushTemplateAndroidPushNotificationTemplateArgs>;
    default?: pulumi.Input<inputs.pinpoint.PushTemplateDefaultPushNotificationTemplateArgs>;
    defaultSubstitutions?: pulumi.Input<string>;
    gcm?: pulumi.Input<inputs.pinpoint.PushTemplateAndroidPushNotificationTemplateArgs>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::PushTemplate` for more information about the expected schema for this property.
     */
    tags?: any;
    templateDescription?: pulumi.Input<string>;
    templateName: pulumi.Input<string>;
}
