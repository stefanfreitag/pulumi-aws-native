// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::EmailTemplate
 *
 * @deprecated EmailTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class EmailTemplate extends pulumi.CustomResource {
    /**
     * Get an existing EmailTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EmailTemplate {
        pulumi.log.warn("EmailTemplate is deprecated: EmailTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new EmailTemplate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpoint:EmailTemplate';

    /**
     * Returns true if the given object is an instance of EmailTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EmailTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EmailTemplate.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly defaultSubstitutions!: pulumi.Output<string | undefined>;
    public readonly htmlPart!: pulumi.Output<string | undefined>;
    public readonly subject!: pulumi.Output<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::EmailTemplate` for more information about the expected schema for this property.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly templateDescription!: pulumi.Output<string | undefined>;
    public readonly templateName!: pulumi.Output<string>;
    public readonly textPart!: pulumi.Output<string | undefined>;

    /**
     * Create a EmailTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated EmailTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: EmailTemplateArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("EmailTemplate is deprecated: EmailTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.subject === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subject'");
            }
            if ((!args || args.templateName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'templateName'");
            }
            resourceInputs["defaultSubstitutions"] = args ? args.defaultSubstitutions : undefined;
            resourceInputs["htmlPart"] = args ? args.htmlPart : undefined;
            resourceInputs["subject"] = args ? args.subject : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["templateDescription"] = args ? args.templateDescription : undefined;
            resourceInputs["templateName"] = args ? args.templateName : undefined;
            resourceInputs["textPart"] = args ? args.textPart : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["defaultSubstitutions"] = undefined /*out*/;
            resourceInputs["htmlPart"] = undefined /*out*/;
            resourceInputs["subject"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["templateDescription"] = undefined /*out*/;
            resourceInputs["templateName"] = undefined /*out*/;
            resourceInputs["textPart"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["templateName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(EmailTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EmailTemplate resource.
 */
export interface EmailTemplateArgs {
    defaultSubstitutions?: pulumi.Input<string>;
    htmlPart?: pulumi.Input<string>;
    subject: pulumi.Input<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::EmailTemplate` for more information about the expected schema for this property.
     */
    tags?: any;
    templateDescription?: pulumi.Input<string>;
    templateName: pulumi.Input<string>;
    textPart?: pulumi.Input<string>;
}
