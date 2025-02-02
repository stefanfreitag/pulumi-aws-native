// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::PinpointEmail::ConfigurationSetEventDestination
 *
 * @deprecated ConfigurationSetEventDestination is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ConfigurationSetEventDestination extends pulumi.CustomResource {
    /**
     * Get an existing ConfigurationSetEventDestination resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConfigurationSetEventDestination {
        pulumi.log.warn("ConfigurationSetEventDestination is deprecated: ConfigurationSetEventDestination is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ConfigurationSetEventDestination(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpointemail:ConfigurationSetEventDestination';

    /**
     * Returns true if the given object is an instance of ConfigurationSetEventDestination.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfigurationSetEventDestination {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfigurationSetEventDestination.__pulumiType;
    }

    public readonly configurationSetName!: pulumi.Output<string>;
    public readonly eventDestination!: pulumi.Output<outputs.pinpointemail.ConfigurationSetEventDestinationEventDestination | undefined>;
    public readonly eventDestinationName!: pulumi.Output<string>;

    /**
     * Create a ConfigurationSetEventDestination resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ConfigurationSetEventDestination is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ConfigurationSetEventDestinationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ConfigurationSetEventDestination is deprecated: ConfigurationSetEventDestination is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.configurationSetName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configurationSetName'");
            }
            if ((!args || args.eventDestinationName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'eventDestinationName'");
            }
            resourceInputs["configurationSetName"] = args ? args.configurationSetName : undefined;
            resourceInputs["eventDestination"] = args ? args.eventDestination : undefined;
            resourceInputs["eventDestinationName"] = args ? args.eventDestinationName : undefined;
        } else {
            resourceInputs["configurationSetName"] = undefined /*out*/;
            resourceInputs["eventDestination"] = undefined /*out*/;
            resourceInputs["eventDestinationName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["configurationSetName", "eventDestinationName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConfigurationSetEventDestination.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConfigurationSetEventDestination resource.
 */
export interface ConfigurationSetEventDestinationArgs {
    configurationSetName: pulumi.Input<string>;
    eventDestination?: pulumi.Input<inputs.pinpointemail.ConfigurationSetEventDestinationEventDestinationArgs>;
    eventDestinationName: pulumi.Input<string>;
}
