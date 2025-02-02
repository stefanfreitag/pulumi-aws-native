// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for StateMachineAlias
 */
export class StateMachineAlias extends pulumi.CustomResource {
    /**
     * Get an existing StateMachineAlias resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StateMachineAlias {
        return new StateMachineAlias(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:stepfunctions:StateMachineAlias';

    /**
     * Returns true if the given object is an instance of StateMachineAlias.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StateMachineAlias {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StateMachineAlias.__pulumiType;
    }

    /**
     * The ARN of the alias.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly deploymentPreference!: pulumi.Output<outputs.stepfunctions.StateMachineAliasDeploymentPreference | undefined>;
    /**
     * An optional description of the alias.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The alias name.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly routingConfiguration!: pulumi.Output<outputs.stepfunctions.StateMachineAliasRoutingConfigurationVersion[] | undefined>;

    /**
     * Create a StateMachineAlias resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: StateMachineAliasArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["deploymentPreference"] = args ? args.deploymentPreference : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["routingConfiguration"] = args ? args.routingConfiguration : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["deploymentPreference"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["routingConfiguration"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(StateMachineAlias.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a StateMachineAlias resource.
 */
export interface StateMachineAliasArgs {
    deploymentPreference?: pulumi.Input<inputs.stepfunctions.StateMachineAliasDeploymentPreferenceArgs>;
    /**
     * An optional description of the alias.
     */
    description?: pulumi.Input<string>;
    /**
     * The alias name.
     */
    name?: pulumi.Input<string>;
    routingConfiguration?: pulumi.Input<pulumi.Input<inputs.stepfunctions.StateMachineAliasRoutingConfigurationVersionArgs>[]>;
}
