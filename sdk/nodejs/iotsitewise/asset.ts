// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::IoTSiteWise::Asset
 */
export class Asset extends pulumi.CustomResource {
    /**
     * Get an existing Asset resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Asset {
        return new Asset(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotsitewise:Asset';

    /**
     * Returns true if the given object is an instance of Asset.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Asset {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Asset.__pulumiType;
    }

    /**
     * The ARN of the asset
     */
    public /*out*/ readonly assetArn!: pulumi.Output<string>;
    public readonly assetHierarchies!: pulumi.Output<outputs.iotsitewise.AssetAssetHierarchy[] | undefined>;
    /**
     * The ID of the asset
     */
    public /*out*/ readonly assetId!: pulumi.Output<string>;
    /**
     * The ID of the asset model from which to create the asset.
     */
    public readonly assetModelId!: pulumi.Output<string>;
    /**
     * A unique, friendly name for the asset.
     */
    public readonly assetName!: pulumi.Output<string>;
    public readonly assetProperties!: pulumi.Output<outputs.iotsitewise.AssetAssetProperty[] | undefined>;
    /**
     * A list of key-value pairs that contain metadata for the asset.
     */
    public readonly tags!: pulumi.Output<outputs.iotsitewise.AssetTag[] | undefined>;

    /**
     * Create a Asset resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AssetArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.assetModelId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'assetModelId'");
            }
            if ((!args || args.assetName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'assetName'");
            }
            inputs["assetHierarchies"] = args ? args.assetHierarchies : undefined;
            inputs["assetModelId"] = args ? args.assetModelId : undefined;
            inputs["assetName"] = args ? args.assetName : undefined;
            inputs["assetProperties"] = args ? args.assetProperties : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["assetArn"] = undefined /*out*/;
            inputs["assetId"] = undefined /*out*/;
        } else {
            inputs["assetArn"] = undefined /*out*/;
            inputs["assetHierarchies"] = undefined /*out*/;
            inputs["assetId"] = undefined /*out*/;
            inputs["assetModelId"] = undefined /*out*/;
            inputs["assetName"] = undefined /*out*/;
            inputs["assetProperties"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Asset.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Asset resource.
 */
export interface AssetArgs {
    assetHierarchies?: pulumi.Input<pulumi.Input<inputs.iotsitewise.AssetAssetHierarchyArgs>[]>;
    /**
     * The ID of the asset model from which to create the asset.
     */
    assetModelId: pulumi.Input<string>;
    /**
     * A unique, friendly name for the asset.
     */
    assetName: pulumi.Input<string>;
    assetProperties?: pulumi.Input<pulumi.Input<inputs.iotsitewise.AssetAssetPropertyArgs>[]>;
    /**
     * A list of key-value pairs that contain metadata for the asset.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.iotsitewise.AssetTagArgs>[]>;
}
