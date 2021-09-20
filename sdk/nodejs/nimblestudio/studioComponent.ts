// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::NimbleStudio::StudioComponent.
 */
export class StudioComponent extends pulumi.CustomResource {
    /**
     * Get an existing StudioComponent resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StudioComponent {
        return new StudioComponent(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:nimblestudio:StudioComponent';

    /**
     * Returns true if the given object is an instance of StudioComponent.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StudioComponent {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StudioComponent.__pulumiType;
    }

    public readonly configuration!: pulumi.Output<outputs.nimblestudio.StudioComponentStudioComponentConfiguration | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly ec2SecurityGroupIds!: pulumi.Output<string[] | undefined>;
    public readonly initializationScripts!: pulumi.Output<outputs.nimblestudio.StudioComponentStudioComponentInitializationScript[] | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly scriptParameters!: pulumi.Output<outputs.nimblestudio.StudioComponentScriptParameterKeyValue[] | undefined>;
    public /*out*/ readonly studioComponentId!: pulumi.Output<string>;
    public readonly studioId!: pulumi.Output<string>;
    public readonly subtype!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a StudioComponent resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StudioComponentArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.studioId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'studioId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            inputs["configuration"] = args ? args.configuration : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["ec2SecurityGroupIds"] = args ? args.ec2SecurityGroupIds : undefined;
            inputs["initializationScripts"] = args ? args.initializationScripts : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["scriptParameters"] = args ? args.scriptParameters : undefined;
            inputs["studioId"] = args ? args.studioId : undefined;
            inputs["subtype"] = args ? args.subtype : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["studioComponentId"] = undefined /*out*/;
        } else {
            inputs["configuration"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["ec2SecurityGroupIds"] = undefined /*out*/;
            inputs["initializationScripts"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["scriptParameters"] = undefined /*out*/;
            inputs["studioComponentId"] = undefined /*out*/;
            inputs["studioId"] = undefined /*out*/;
            inputs["subtype"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(StudioComponent.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a StudioComponent resource.
 */
export interface StudioComponentArgs {
    configuration?: pulumi.Input<inputs.nimblestudio.StudioComponentStudioComponentConfigurationArgs>;
    description?: pulumi.Input<string>;
    ec2SecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    initializationScripts?: pulumi.Input<pulumi.Input<inputs.nimblestudio.StudioComponentStudioComponentInitializationScriptArgs>[]>;
    name: pulumi.Input<string>;
    scriptParameters?: pulumi.Input<pulumi.Input<inputs.nimblestudio.StudioComponentScriptParameterKeyValueArgs>[]>;
    studioId: pulumi.Input<string>;
    subtype?: pulumi.Input<string>;
    tags?: any;
    type: pulumi.Input<string>;
}
