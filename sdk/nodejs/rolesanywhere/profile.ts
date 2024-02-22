// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::RolesAnywhere::Profile Resource Type
 */
export class Profile extends pulumi.CustomResource {
    /**
     * Get an existing Profile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Profile {
        return new Profile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rolesanywhere:Profile';

    /**
     * Returns true if the given object is an instance of Profile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Profile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Profile.__pulumiType;
    }

    public readonly durationSeconds!: pulumi.Output<number | undefined>;
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    public readonly managedPolicyArns!: pulumi.Output<string[] | undefined>;
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly profileArn!: pulumi.Output<string>;
    public /*out*/ readonly profileId!: pulumi.Output<string>;
    public readonly requireInstanceProperties!: pulumi.Output<boolean | undefined>;
    public readonly roleArns!: pulumi.Output<string[]>;
    public readonly sessionPolicy!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Profile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProfileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.roleArns === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArns'");
            }
            resourceInputs["durationSeconds"] = args ? args.durationSeconds : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["managedPolicyArns"] = args ? args.managedPolicyArns : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["requireInstanceProperties"] = args ? args.requireInstanceProperties : undefined;
            resourceInputs["roleArns"] = args ? args.roleArns : undefined;
            resourceInputs["sessionPolicy"] = args ? args.sessionPolicy : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["profileArn"] = undefined /*out*/;
            resourceInputs["profileId"] = undefined /*out*/;
        } else {
            resourceInputs["durationSeconds"] = undefined /*out*/;
            resourceInputs["enabled"] = undefined /*out*/;
            resourceInputs["managedPolicyArns"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["profileArn"] = undefined /*out*/;
            resourceInputs["profileId"] = undefined /*out*/;
            resourceInputs["requireInstanceProperties"] = undefined /*out*/;
            resourceInputs["roleArns"] = undefined /*out*/;
            resourceInputs["sessionPolicy"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Profile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Profile resource.
 */
export interface ProfileArgs {
    durationSeconds?: pulumi.Input<number>;
    enabled?: pulumi.Input<boolean>;
    managedPolicyArns?: pulumi.Input<pulumi.Input<string>[]>;
    name?: pulumi.Input<string>;
    requireInstanceProperties?: pulumi.Input<boolean>;
    roleArns: pulumi.Input<pulumi.Input<string>[]>;
    sessionPolicy?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
