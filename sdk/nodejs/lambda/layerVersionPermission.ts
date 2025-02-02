// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Schema for Lambda LayerVersionPermission
 */
export class LayerVersionPermission extends pulumi.CustomResource {
    /**
     * Get an existing LayerVersionPermission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LayerVersionPermission {
        return new LayerVersionPermission(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lambda:LayerVersionPermission';

    /**
     * Returns true if the given object is an instance of LayerVersionPermission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LayerVersionPermission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LayerVersionPermission.__pulumiType;
    }

    /**
     * The API action that grants access to the layer.
     */
    public readonly action!: pulumi.Output<string>;
    /**
     * The name or Amazon Resource Name (ARN) of the layer.
     */
    public readonly layerVersionArn!: pulumi.Output<string>;
    /**
     * With the principal set to *, grant permission to all accounts in the specified organization.
     */
    public readonly organizationId!: pulumi.Output<string | undefined>;
    /**
     * An account ID, or * to grant layer usage permission to all accounts in an organization, or all AWS accounts (if organizationId is not specified).
     */
    public readonly principal!: pulumi.Output<string>;

    /**
     * Create a LayerVersionPermission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LayerVersionPermissionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.action === undefined) && !opts.urn) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.layerVersionArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'layerVersionArn'");
            }
            if ((!args || args.principal === undefined) && !opts.urn) {
                throw new Error("Missing required property 'principal'");
            }
            resourceInputs["action"] = args ? args.action : undefined;
            resourceInputs["layerVersionArn"] = args ? args.layerVersionArn : undefined;
            resourceInputs["organizationId"] = args ? args.organizationId : undefined;
            resourceInputs["principal"] = args ? args.principal : undefined;
        } else {
            resourceInputs["action"] = undefined /*out*/;
            resourceInputs["layerVersionArn"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["principal"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["action", "layerVersionArn", "organizationId", "principal"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(LayerVersionPermission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a LayerVersionPermission resource.
 */
export interface LayerVersionPermissionArgs {
    /**
     * The API action that grants access to the layer.
     */
    action: pulumi.Input<string>;
    /**
     * The name or Amazon Resource Name (ARN) of the layer.
     */
    layerVersionArn: pulumi.Input<string>;
    /**
     * With the principal set to *, grant permission to all accounts in the specified organization.
     */
    organizationId?: pulumi.Input<string>;
    /**
     * An account ID, or * to grant layer usage permission to all accounts in an organization, or all AWS accounts (if organizationId is not specified).
     */
    principal: pulumi.Input<string>;
}
