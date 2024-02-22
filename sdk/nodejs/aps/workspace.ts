// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::APS::Workspace
 */
export class Workspace extends pulumi.CustomResource {
    /**
     * Get an existing Workspace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Workspace {
        return new Workspace(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:aps:Workspace';

    /**
     * Returns true if the given object is an instance of Workspace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Workspace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Workspace.__pulumiType;
    }

    /**
     * The AMP Workspace alert manager definition data
     */
    public readonly alertManagerDefinition!: pulumi.Output<string | undefined>;
    /**
     * AMP Workspace alias.
     */
    public readonly alias!: pulumi.Output<string | undefined>;
    /**
     * Workspace arn.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * KMS Key ARN used to encrypt and decrypt AMP workspace data.
     */
    public readonly kmsKeyArn!: pulumi.Output<string | undefined>;
    public readonly loggingConfiguration!: pulumi.Output<outputs.aps.WorkspaceLoggingConfiguration | undefined>;
    /**
     * AMP Workspace prometheus endpoint
     */
    public /*out*/ readonly prometheusEndpoint!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * Required to identify a specific APS Workspace.
     */
    public /*out*/ readonly workspaceId!: pulumi.Output<string>;

    /**
     * Create a Workspace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: WorkspaceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["alertManagerDefinition"] = args ? args.alertManagerDefinition : undefined;
            resourceInputs["alias"] = args ? args.alias : undefined;
            resourceInputs["kmsKeyArn"] = args ? args.kmsKeyArn : undefined;
            resourceInputs["loggingConfiguration"] = args ? args.loggingConfiguration : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["prometheusEndpoint"] = undefined /*out*/;
            resourceInputs["workspaceId"] = undefined /*out*/;
        } else {
            resourceInputs["alertManagerDefinition"] = undefined /*out*/;
            resourceInputs["alias"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["kmsKeyArn"] = undefined /*out*/;
            resourceInputs["loggingConfiguration"] = undefined /*out*/;
            resourceInputs["prometheusEndpoint"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["workspaceId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["kmsKeyArn"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Workspace.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Workspace resource.
 */
export interface WorkspaceArgs {
    /**
     * The AMP Workspace alert manager definition data
     */
    alertManagerDefinition?: pulumi.Input<string>;
    /**
     * AMP Workspace alias.
     */
    alias?: pulumi.Input<string>;
    /**
     * KMS Key ARN used to encrypt and decrypt AMP workspace data.
     */
    kmsKeyArn?: pulumi.Input<string>;
    loggingConfiguration?: pulumi.Input<inputs.aps.WorkspaceLoggingConfigurationArgs>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
