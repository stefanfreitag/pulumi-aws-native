// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.
 */
export class RoleAlias extends pulumi.CustomResource {
    /**
     * Get an existing RoleAlias resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): RoleAlias {
        return new RoleAlias(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:RoleAlias';

    /**
     * Returns true if the given object is an instance of RoleAlias.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RoleAlias {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RoleAlias.__pulumiType;
    }

    public readonly credentialDurationSeconds!: pulumi.Output<number | undefined>;
    public readonly roleAlias!: pulumi.Output<string | undefined>;
    public /*out*/ readonly roleAliasArn!: pulumi.Output<string>;
    public readonly roleArn!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.iot.RoleAliasTag[] | undefined>;

    /**
     * Create a RoleAlias resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RoleAliasArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            resourceInputs["credentialDurationSeconds"] = args ? args.credentialDurationSeconds : undefined;
            resourceInputs["roleAlias"] = args ? args.roleAlias : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["roleAliasArn"] = undefined /*out*/;
        } else {
            resourceInputs["credentialDurationSeconds"] = undefined /*out*/;
            resourceInputs["roleAlias"] = undefined /*out*/;
            resourceInputs["roleAliasArn"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RoleAlias.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a RoleAlias resource.
 */
export interface RoleAliasArgs {
    credentialDurationSeconds?: pulumi.Input<number>;
    roleAlias?: pulumi.Input<string>;
    roleArn: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.iot.RoleAliasTagArgs>[]>;
}
