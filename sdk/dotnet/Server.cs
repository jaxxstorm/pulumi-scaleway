// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    /// <summary>
    /// **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
    /// Please use `scaleway.InstanceServer` instead.
    /// 
    /// Provides servers. This allows servers to be created, updated and deleted.
    /// For additional details please refer to [API documentation](https://developer.scaleway.com/#servers).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Scaleway = Pulumi.Scaleway;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var test = new Scaleway.Server("test", new Scaleway.ServerArgs
    ///         {
    ///             Image = "5faef9cd-ea9b-4a63-9171-9e26bec03dbc",
    ///             Type = "VC1M",
    ///             Volumes = 
    ///             {
    ///                 new Scaleway.Inputs.ServerVolumeArgs
    ///                 {
    ///                     SizeInGb = 20,
    ///                     Type = "l_ssd",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Volume
    /// 
    /// You can attach additional volumes to your instance, which will share the lifetime
    /// of your `scaleway.Server` resource.
    /// 
    /// &gt; **Warning:** Using the `volume` attribute does not modify the System Volume provided default with every `scaleway.Server` instance. Instead it adds additional volumes to the server instance.
    /// 
    /// &gt; **Warning:** Some instance types require an additional volume to work. This includes for example *START-1M* and *VC1M*. If you run into this issue add an additional volume of the specified size.
    /// 
    /// The `volume` mapping supports the following:
    /// 
    /// * `type` - (Required) The type of volume. Can be `"l_ssd"`
    /// * `size_in_gb` - (Required) The size of the volume in gigabytes.
    /// </summary>
    public partial class Server : Pulumi.CustomResource
    {
        /// <summary>
        /// the boot mechanism for this server. Possible values include `local` and `bootscript`
        /// </summary>
        [Output("bootType")]
        public Output<string> BootType { get; private set; } = null!;

        /// <summary>
        /// server bootscript
        /// </summary>
        [Output("bootscript")]
        public Output<string?> Bootscript { get; private set; } = null!;

        /// <summary>
        /// allows you to define cloudinit script for this server
        /// </summary>
        [Output("cloudinit")]
        public Output<string> Cloudinit { get; private set; } = null!;

        /// <summary>
        /// make server publicly available
        /// </summary>
        [Output("dynamicIpRequired")]
        public Output<bool?> DynamicIpRequired { get; private set; } = null!;

        /// <summary>
        /// enable ipv6
        /// </summary>
        [Output("enableIpv6")]
        public Output<bool?> EnableIpv6 { get; private set; } = null!;

        /// <summary>
        /// base image of server
        /// </summary>
        [Output("image")]
        public Output<string> Image { get; private set; } = null!;

        /// <summary>
        /// name of server
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// private ip of the new resource
        /// </summary>
        [Output("privateIp")]
        public Output<string> PrivateIp { get; private set; } = null!;

        /// <summary>
        /// set a public ip previously created (a real ip is expected here, not its resource id)
        /// </summary>
        [Output("publicIp")]
        public Output<string> PublicIp { get; private set; } = null!;

        /// <summary>
        /// if `enable_ipv6` is set this contains the ipv6 address of your instance
        /// </summary>
        [Output("publicIpv6")]
        public Output<string> PublicIpv6 { get; private set; } = null!;

        /// <summary>
        /// assign security group to server
        /// </summary>
        [Output("securityGroup")]
        public Output<string?> SecurityGroup { get; private set; } = null!;

        /// <summary>
        /// allows you to define the desired state of your server. Valid values include (`stopped`, `running`)
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// contains details from the scaleway API the state of your instance
        /// </summary>
        [Output("stateDetail")]
        public Output<string> StateDetail { get; private set; } = null!;

        /// <summary>
        /// list of tags for server
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// type of server
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// attach additional volumes to your instance (see below)
        /// </summary>
        [Output("volumes")]
        public Output<ImmutableArray<Outputs.ServerVolume>> Volumes { get; private set; } = null!;


        /// <summary>
        /// Create a Server resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Server(string name, ServerArgs args, CustomResourceOptions? options = null)
            : base("scaleway:index/server:Server", name, args ?? new ServerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Server(string name, Input<string> id, ServerState? state = null, CustomResourceOptions? options = null)
            : base("scaleway:index/server:Server", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Server resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Server Get(string name, Input<string> id, ServerState? state = null, CustomResourceOptions? options = null)
        {
            return new Server(name, id, state, options);
        }
    }

    public sealed class ServerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// the boot mechanism for this server. Possible values include `local` and `bootscript`
        /// </summary>
        [Input("bootType")]
        public Input<string>? BootType { get; set; }

        /// <summary>
        /// server bootscript
        /// </summary>
        [Input("bootscript")]
        public Input<string>? Bootscript { get; set; }

        /// <summary>
        /// allows you to define cloudinit script for this server
        /// </summary>
        [Input("cloudinit")]
        public Input<string>? Cloudinit { get; set; }

        /// <summary>
        /// make server publicly available
        /// </summary>
        [Input("dynamicIpRequired")]
        public Input<bool>? DynamicIpRequired { get; set; }

        /// <summary>
        /// enable ipv6
        /// </summary>
        [Input("enableIpv6")]
        public Input<bool>? EnableIpv6 { get; set; }

        /// <summary>
        /// base image of server
        /// </summary>
        [Input("image", required: true)]
        public Input<string> Image { get; set; } = null!;

        /// <summary>
        /// name of server
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// set a public ip previously created (a real ip is expected here, not its resource id)
        /// </summary>
        [Input("publicIp")]
        public Input<string>? PublicIp { get; set; }

        /// <summary>
        /// assign security group to server
        /// </summary>
        [Input("securityGroup")]
        public Input<string>? SecurityGroup { get; set; }

        /// <summary>
        /// allows you to define the desired state of your server. Valid values include (`stopped`, `running`)
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// list of tags for server
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// type of server
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("volumes")]
        private InputList<Inputs.ServerVolumeArgs>? _volumes;

        /// <summary>
        /// attach additional volumes to your instance (see below)
        /// </summary>
        public InputList<Inputs.ServerVolumeArgs> Volumes
        {
            get => _volumes ?? (_volumes = new InputList<Inputs.ServerVolumeArgs>());
            set => _volumes = value;
        }

        public ServerArgs()
        {
        }
    }

    public sealed class ServerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// the boot mechanism for this server. Possible values include `local` and `bootscript`
        /// </summary>
        [Input("bootType")]
        public Input<string>? BootType { get; set; }

        /// <summary>
        /// server bootscript
        /// </summary>
        [Input("bootscript")]
        public Input<string>? Bootscript { get; set; }

        /// <summary>
        /// allows you to define cloudinit script for this server
        /// </summary>
        [Input("cloudinit")]
        public Input<string>? Cloudinit { get; set; }

        /// <summary>
        /// make server publicly available
        /// </summary>
        [Input("dynamicIpRequired")]
        public Input<bool>? DynamicIpRequired { get; set; }

        /// <summary>
        /// enable ipv6
        /// </summary>
        [Input("enableIpv6")]
        public Input<bool>? EnableIpv6 { get; set; }

        /// <summary>
        /// base image of server
        /// </summary>
        [Input("image")]
        public Input<string>? Image { get; set; }

        /// <summary>
        /// name of server
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// private ip of the new resource
        /// </summary>
        [Input("privateIp")]
        public Input<string>? PrivateIp { get; set; }

        /// <summary>
        /// set a public ip previously created (a real ip is expected here, not its resource id)
        /// </summary>
        [Input("publicIp")]
        public Input<string>? PublicIp { get; set; }

        /// <summary>
        /// if `enable_ipv6` is set this contains the ipv6 address of your instance
        /// </summary>
        [Input("publicIpv6")]
        public Input<string>? PublicIpv6 { get; set; }

        /// <summary>
        /// assign security group to server
        /// </summary>
        [Input("securityGroup")]
        public Input<string>? SecurityGroup { get; set; }

        /// <summary>
        /// allows you to define the desired state of your server. Valid values include (`stopped`, `running`)
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// contains details from the scaleway API the state of your instance
        /// </summary>
        [Input("stateDetail")]
        public Input<string>? StateDetail { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// list of tags for server
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// type of server
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("volumes")]
        private InputList<Inputs.ServerVolumeGetArgs>? _volumes;

        /// <summary>
        /// attach additional volumes to your instance (see below)
        /// </summary>
        public InputList<Inputs.ServerVolumeGetArgs> Volumes
        {
            get => _volumes ?? (_volumes = new InputList<Inputs.ServerVolumeGetArgs>());
            set => _volumes = value;
        }

        public ServerState()
        {
        }
    }
}
