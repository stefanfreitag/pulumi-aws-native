// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::OpsWorks::Layer
 *
 * @deprecated Layer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Layer extends pulumi.CustomResource {
    /**
     * Get an existing Layer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Layer {
        pulumi.log.warn("Layer is deprecated: Layer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Layer(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:opsworks:Layer';

    /**
     * Returns true if the given object is an instance of Layer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Layer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Layer.__pulumiType;
    }

    public readonly attributes!: pulumi.Output<any | undefined>;
    public readonly autoAssignElasticIps!: pulumi.Output<boolean>;
    public readonly autoAssignPublicIps!: pulumi.Output<boolean>;
    public readonly customInstanceProfileArn!: pulumi.Output<string | undefined>;
    public readonly customJson!: pulumi.Output<any | undefined>;
    public readonly customRecipes!: pulumi.Output<outputs.opsworks.LayerRecipes | undefined>;
    public readonly customSecurityGroupIds!: pulumi.Output<string[] | undefined>;
    public readonly enableAutoHealing!: pulumi.Output<boolean>;
    public readonly installUpdatesOnBoot!: pulumi.Output<boolean | undefined>;
    public readonly lifecycleEventConfiguration!: pulumi.Output<outputs.opsworks.LayerLifecycleEventConfiguration | undefined>;
    public readonly loadBasedAutoScaling!: pulumi.Output<outputs.opsworks.LayerLoadBasedAutoScaling | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly packages!: pulumi.Output<string[] | undefined>;
    public readonly shortname!: pulumi.Output<string>;
    public readonly stackId!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.opsworks.LayerTag[] | undefined>;
    public readonly type!: pulumi.Output<string>;
    public readonly useEbsOptimizedInstances!: pulumi.Output<boolean | undefined>;
    public readonly volumeConfigurations!: pulumi.Output<outputs.opsworks.LayerVolumeConfiguration[] | undefined>;

    /**
     * Create a Layer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Layer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: LayerArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Layer is deprecated: Layer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.autoAssignElasticIps === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoAssignElasticIps'");
            }
            if ((!args || args.autoAssignPublicIps === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoAssignPublicIps'");
            }
            if ((!args || args.enableAutoHealing === undefined) && !opts.urn) {
                throw new Error("Missing required property 'enableAutoHealing'");
            }
            if ((!args || args.shortname === undefined) && !opts.urn) {
                throw new Error("Missing required property 'shortname'");
            }
            if ((!args || args.stackId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stackId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["attributes"] = args ? args.attributes : undefined;
            resourceInputs["autoAssignElasticIps"] = args ? args.autoAssignElasticIps : undefined;
            resourceInputs["autoAssignPublicIps"] = args ? args.autoAssignPublicIps : undefined;
            resourceInputs["customInstanceProfileArn"] = args ? args.customInstanceProfileArn : undefined;
            resourceInputs["customJson"] = args ? args.customJson : undefined;
            resourceInputs["customRecipes"] = args ? args.customRecipes : undefined;
            resourceInputs["customSecurityGroupIds"] = args ? args.customSecurityGroupIds : undefined;
            resourceInputs["enableAutoHealing"] = args ? args.enableAutoHealing : undefined;
            resourceInputs["installUpdatesOnBoot"] = args ? args.installUpdatesOnBoot : undefined;
            resourceInputs["lifecycleEventConfiguration"] = args ? args.lifecycleEventConfiguration : undefined;
            resourceInputs["loadBasedAutoScaling"] = args ? args.loadBasedAutoScaling : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["packages"] = args ? args.packages : undefined;
            resourceInputs["shortname"] = args ? args.shortname : undefined;
            resourceInputs["stackId"] = args ? args.stackId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["useEbsOptimizedInstances"] = args ? args.useEbsOptimizedInstances : undefined;
            resourceInputs["volumeConfigurations"] = args ? args.volumeConfigurations : undefined;
        } else {
            resourceInputs["attributes"] = undefined /*out*/;
            resourceInputs["autoAssignElasticIps"] = undefined /*out*/;
            resourceInputs["autoAssignPublicIps"] = undefined /*out*/;
            resourceInputs["customInstanceProfileArn"] = undefined /*out*/;
            resourceInputs["customJson"] = undefined /*out*/;
            resourceInputs["customRecipes"] = undefined /*out*/;
            resourceInputs["customSecurityGroupIds"] = undefined /*out*/;
            resourceInputs["enableAutoHealing"] = undefined /*out*/;
            resourceInputs["installUpdatesOnBoot"] = undefined /*out*/;
            resourceInputs["lifecycleEventConfiguration"] = undefined /*out*/;
            resourceInputs["loadBasedAutoScaling"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["packages"] = undefined /*out*/;
            resourceInputs["shortname"] = undefined /*out*/;
            resourceInputs["stackId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["useEbsOptimizedInstances"] = undefined /*out*/;
            resourceInputs["volumeConfigurations"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Layer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Layer resource.
 */
export interface LayerArgs {
    attributes?: any;
    autoAssignElasticIps: pulumi.Input<boolean>;
    autoAssignPublicIps: pulumi.Input<boolean>;
    customInstanceProfileArn?: pulumi.Input<string>;
    customJson?: any;
    customRecipes?: pulumi.Input<inputs.opsworks.LayerRecipesArgs>;
    customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    enableAutoHealing: pulumi.Input<boolean>;
    installUpdatesOnBoot?: pulumi.Input<boolean>;
    lifecycleEventConfiguration?: pulumi.Input<inputs.opsworks.LayerLifecycleEventConfigurationArgs>;
    loadBasedAutoScaling?: pulumi.Input<inputs.opsworks.LayerLoadBasedAutoScalingArgs>;
    name?: pulumi.Input<string>;
    packages?: pulumi.Input<pulumi.Input<string>[]>;
    shortname: pulumi.Input<string>;
    stackId: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.opsworks.LayerTagArgs>[]>;
    type: pulumi.Input<string>;
    useEbsOptimizedInstances?: pulumi.Input<boolean>;
    volumeConfigurations?: pulumi.Input<pulumi.Input<inputs.opsworks.LayerVolumeConfigurationArgs>[]>;
}
